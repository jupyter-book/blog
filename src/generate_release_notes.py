#!/usr/bin/env python3
"""
Script to generate release notes from GitHub releases in the jupyter-book org.
"""

import json
import re
import subprocess
import sys
import shutil
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path


def normalize_title(text):
    """Normalize a title for loose comparisons."""
    return re.sub(r"[^0-9a-z]+", "", text.lower().lstrip("v"))


def slugify(value):
    """Return a filesystem-safe slug."""
    return re.sub(r"[^a-zA-Z0-9-.]", "-", value.lower())


def split_leading_header(body):
    """Return (level, title) and body without that header when one is leading."""
    if not body:
        return None, body

    lines = body.splitlines()
    for index, line in enumerate(lines):
        if not line.strip():
            continue

        match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if not match:
            return None, body

        level = len(match.group(1))
        title = match.group(2).strip()
        remaining = lines[:index] + lines[index + 1 :]
        if index < len(remaining) and not remaining[index].strip():
            remaining.pop(index)

        return (level, title), "\n".join(remaining)

    return None, body


def resolve_release_title(release_title, release_version, body):
    """Use a leading H1 as the title and strip duplicated header lines."""
    header, body_without_header = split_leading_header(body)
    if not header:
        return release_title, body

    header_level, header_title = header
    header_norm = normalize_title(header_title)
    title_norm = normalize_title(release_title)
    version_norm = normalize_title(release_version)
    header_matches = (
        header_norm == title_norm
        or header_norm == version_norm
        or (title_norm and title_norm in header_norm)
        or (version_norm and version_norm in header_norm)
    )

    if header_level == 1:
        return header_title, body_without_header
    if header_matches:
        return release_title, body_without_header

    return release_title, body


def clean_release_body(body):
    """Remove boilerplate sections and lines from release notes."""
    if not body:
        return body

    lines = body.splitlines()
    cleaned = []
    skip_level = None

    for line in lines:
        match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip().lower()

            if skip_level is not None and level <= skip_level:
                skip_level = None
            if skip_level is None and "contributors to this release" in title:
                skip_level = level
                continue
            if skip_level is not None:
                continue

        if skip_level is not None:
            continue

        lowered = line.lower()
        if "full changelog" in lowered:
            continue
        if "contributors page for this release" in lowered:
            continue
        if "definition of contributors" in lowered:
            continue

        cleaned.append(line)

    return "\n".join(cleaned)


def bold_headers(body):
    """Convert markdown headers to bold lines (outside fenced code blocks)."""
    if not body:
        return body

    lines = body.splitlines()
    in_fence = False
    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if match:
            lines[index] = f"**{match.group(2).strip()}**"

    return "\n".join(lines)


def normalize_repo_title(repo_name, title):
    """Add repository name to a title if it isn't already present."""
    normalized_repo = normalize_title(repo_name)
    normalized_title = normalize_title(title)

    return title if normalized_repo in normalized_title else f"{repo_name} {title}"


def extract_version(tag_name):
    """Extract a version-like string from a tag name."""
    match = re.search(r"v?\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", tag_name)
    return match.group(0) if match else tag_name


def format_table_cell(value):
    """Prepare a value for markdown tables."""
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def main():
    # Check if gh command exists
    try:
        subprocess.run(["gh", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: GitHub CLI (gh) is not installed or not available in PATH")
        print("Please install it from: https://cli.github.com/")
        sys.exit(1)

    # Configuration
    org = "jupyter-book"
    releases_dir = Path("docs/releases")
    raw_releases_dir = Path("docs/_build/releases")
    months_window = 12

    # Keep generated content in docs/ and raw downloads in docs/_build.
    for directory in (releases_dir, raw_releases_dir):
        if directory.exists():
            shutil.rmtree(directory)
        directory.mkdir(parents=True, exist_ok=True)

    print(f"Fetching all repositories from {org} organization...")

    # Fetch all repositories
    try:
        result = subprocess.run(
            ["gh", "api", f"orgs/{org}/repos", "--paginate"],
            capture_output=True,
            text=True,
            check=True,
        )
        repos = json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error fetching repositories: {e}")
        sys.exit(1)

    # Use this to exclude repositories that are particularly noisy we can focus on the marquee projects.
    EXCLUDE_REPOSITORIES = ["myst-plugins", "workshop-template"]
    repos = [repo for repo in repos if repo["name"] not in EXCLUDE_REPOSITORIES]

    print("Fetching releases from all repositories...")

    all_releases = []

    for repo in repos:
        repo_name = repo["name"]
        print(f"Fetching releases from {repo_name}...")

        try:
            result = subprocess.run(
                ["gh", "api", f"repos/{org}/{repo_name}/releases", "--paginate"],
                capture_output=True,
                text=True,
                check=True,
            )
            releases = json.loads(result.stdout)

            for release in releases:
                release["repo_name"] = repo_name
                all_releases.append(release)

        except subprocess.CalledProcessError:
            print(f"No releases found for {repo_name}")
        except json.JSONDecodeError:
            print(f"Error parsing releases for {repo_name}")

    # Only keep releases from the last N months.
    cutoff = datetime.now(timezone.utc) - timedelta(days=365)
    recent_releases = []
    for release in all_releases:
        published_at = release.get("published_at")
        if not published_at:
            continue

        published_dt = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
        if published_dt >= cutoff:
            release["published_dt"] = published_dt
            recent_releases.append(release)

    all_releases = recent_releases
    total = len(all_releases)
    print(f"Found {total} releases from the last {months_window} months")

    # Persist raw release bodies for inspection/debugging.
    print("Writing raw release notes...")
    for release in all_releases:
        repo_name = release["repo_name"]
        tag_name = release["tag_name"]
        safe_tag = slugify(tag_name)
        filename = raw_releases_dir / f"{repo_name}-{safe_tag}.md"
        body = release["body"] or ""

        with open(filename, "w") as f:
            f.write(body)
            if body and not body.endswith("\n"):
                f.write("\n")

    grouped_releases = defaultdict(list)
    for release in all_releases:
        grouped_releases[release["repo_name"]].append(release)

    release_rows = []
    for repo_name, releases in grouped_releases.items():
        releases = sorted(releases, key=lambda r: r["published_at"], reverse=True)
        safe_repo = slugify(repo_name)

        title = repo_name
        url = f"/releases/{safe_repo}"
        filename = releases_dir / f"{safe_repo}.md"
        releases_url = f"https://github.com/{org}/{repo_name}/releases"
        intro = (
            f"These are the latest releases for {repo_name} over the past "
            f"{months_window} months. See [the GitHub releases page]"
            f"({releases_url}) for the full list of all releases."
        )

        # Write the markdown file
        with open(filename, "w") as f:
            f.write("---\n")
            f.write(f"title: {title}\n")
            f.write(f"url: {url}\n")
            f.write(f"repository: {repo_name}\n")
            f.write("tags:\n")
            f.write("  - release\n")
            f.write("---\n\n")
            f.write(f"{intro}\n\n")

            for release in releases:
                release_title = release["name"] or release["tag_name"]
                tag_name = release["tag_name"]
                release_date = release["published_at"][:10]
                release_version = extract_version(tag_name)
                safe_tag = slugify(tag_name)
                label = f"release-{safe_repo}-{safe_tag}"
                body = release["body"] or ""

                release_title, body = resolve_release_title(
                    release_title, release_version, body
                )

                # Normalize content: links and headings are easier to scan this way.
                body = re.sub(r"(?<=[\s(,\[])@(\w+)(?!`)", r"`@\1`", body)
                body = clean_release_body(body)
                body = bold_headers(body)

                f.write(f"({label})=\n")
                f.write(f"## {release_title}\n\n")
                f.write(
                    f"Date: {release_date} | "
                    f"[Release source]({release['html_url']})\n\n"
                )
                f.write(body.strip())
                f.write("\n\n")

                release_rows.append(
                    {
                        "title": normalize_repo_title(repo_name, release_title),
                        "version": release_version,
                        "date": release_date,
                        "github_url": release["html_url"],
                        "section": f"{{ref}}`Release section <{label}>`",
                        "published_dt": release["published_dt"],
                    }
                )

        print(f"Generated: {filename}")

    # Table for the releases index page.
    release_rows = sorted(release_rows, key=lambda r: r["published_dt"], reverse=True)
    table_path = releases_dir / "release-table.txt"
    with open(table_path, "w") as f:
        f.write("| Title | Version | Date | Release source | Section |\n")
        f.write("| --- | --- | --- | --- | --- |\n")
        for row in release_rows:
            f.write(
                "| {title} | {version} | {date} | {source} | {section} |\n".format(
                    title=format_table_cell(row["title"]),
                    version=format_table_cell(row["version"]),
                    date=format_table_cell(row["date"]),
                    source=format_table_cell(f"[GitHub]({row['github_url']})"),
                    section=format_table_cell(row["section"]),
                )
            )

    print("Release posts generated successfully!")


if __name__ == "__main__":
    main()
