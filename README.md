# The Jupyter Book blog

A blog for the Jupyter Book subproject.

## Local development

This blog is a small [MyST site](https://mystmd.org) along with a [javascript plugin for blogging](plugins/blog.mjs).

To run it locally, take these steps:

1. **Install NPM and MyST** by [following the MyST installation instructions](https://mystmd.org/guide/installing).
2. **Install the plugin requirements** with NPM:

   ```shell
   $ npm install
   ```
3. **Build the site**:

   ```shell
   $ myst start
   ```

## Release Posts

The `posts/releases/` folder contains automatically generated release posts for all repositories in the Jupyter Book organization.

### To add release notes to the blog

1. Make the release on GitHub
2. Re-build the blog

The blog action will catch the latest release and include it in the list, sorted by dates.

### How it works

The release posts are generated automatically using the `src/generate_release_notes.py` script, which:

1. **Fetches all repositories** from the `jupyter-book` GitHub organization
2. **Retrieves all releases** from each repository using the GitHub API
3. **Sorts releases by date** (newest first)
4. **Generates numbered markdown files** with proper frontmatter
5. **Formats @mentions** with backticks for better readability
6. **Adds formatted dates** to titles (e.g., "July 6th, 2025")

### File Naming Convention

Files are named with a numbered prefix to ensure proper ordering until we make it possible to list blog posts sorted by date:
- `001-{repo-name}-{release-title}.md` (newest release)
- `002-{repo-name}-{release-title}.md`
- ...
- `224-{repo-name}-{release-title}.md` (oldest release)

### Generating Release Posts

To generate the release posts locally:

```shell
$ python src/generate_release_notes.py
```

**Requirements:**
- GitHub CLI (`gh`) must be installed and authenticated
- Python 3 for processing JSON data

### Automation

The release posts are automatically generated during the CI/CD build process (see `.github/workflows/deploy.yml`). This ensures that new releases are always included in the blog without manual intervention.
