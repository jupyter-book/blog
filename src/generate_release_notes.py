#!/usr/bin/env python3
"""
Script to generate release notes from GitHub releases in the jupyter-book org.
"""

import json
import re
import subprocess
import sys
import shutil
from datetime import datetime
from pathlib import Path


def format_date(date_str):
    """Convert ISO date string to readable format like 'June 17th, 2025'"""
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    # Get month name
    month = date_obj.strftime("%B")

    # Get day with ordinal suffix
    day = date_obj.day
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]

    # Get year
    year = date_obj.year

    return f"{month} {day}{suffix}, {year}"


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
    releases_dir = Path("posts/releases")
    temp_dir = Path("_build/release_notes")

    # Clean and ensure directories exist
    if releases_dir.exists():
        shutil.rmtree(releases_dir)
    releases_dir.mkdir(parents=True, exist_ok=True)
    temp_dir.mkdir(parents=True, exist_ok=True)

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

    # Sort releases by publication date so the largest numbers are the newest.
    # this forces latest releases to the top until we have a proper sorting system.
    all_releases.sort(key=lambda x: x["published_at"], reverse=True)

    total = len(all_releases)
    print(f"Found {total} total releases")

    for ii, release in enumerate(all_releases):
        number = ii + 1
        title = release["name"] or release["tag_name"]
        repo_name = release["repo_name"]

        # Add repository name to title if it's not already present
        # Normalize both strings by replacing hyphens, underscores, and spaces
        normalized_repo = (
            repo_name.lower().replace("-", "").replace("_", "").replace(" ", "")
        )
        normalized_title = (
            title.lower().replace("-", "").replace("_", "").replace(" ", "")
        )

        if normalized_repo not in normalized_title:
            title = f"{repo_name} {title}"

        date = release["published_at"][:10]
        formatted_date = format_date(date)
        title = f"{title} - {formatted_date}"
        body = release["body"] or ""

        # Wrap @mentions in backticks (only if preceded by space, (, comma, or [, and not already wrapped)
        body = re.sub(r"(?<=[\s(,\[])@(\w+)(?!`)", r"`@\1`", body)

        # Create filename
        safe_title = re.sub(r"[^a-zA-Z0-9-]", "-", title.lower())
        filename = releases_dir / f"{number:03d}-{repo_name}-{safe_title}.md"

        # Write the markdown file
        with open(filename, "w") as f:
            f.write("---\n")
            f.write(f"title: {title}\n")
            f.write(f"date: {date}\n")
            f.write("author: The Jupyter Book Team\n")
            f.write("tags:\n")
            f.write("  - release\n")
            f.write("---\n\n")
            f.write(body)
            f.write("\n")

        print(f"Generated: {filename}")

    print("Release posts generated successfully!")


if __name__ == "__main__":
    main()
