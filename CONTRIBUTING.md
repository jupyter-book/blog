# Contributing to the Jupyter Book Blog

Our blog is our primary mechanism for recording what we do and the impact we've had. It also gives us a record of our work that we can quickly use for generating reports.

## Principles to follow

- Shorter, imperfect, and more frequent
- If you're not sure whether it's in scope, it's probably in scope
- Link to other places to learn more

## Things to blog about

- Examples of Jupyter Book having impact "in the wild"
- Share updates of our work (this can be super small! it is more interesting than you imagine!)
- Share learning and inspiration that's relevant to Jupyter Book

## Share an idea for a blog post

Anybody is encouraged to share blog post ideas!
Fill out the [blog post issue template](https://github.com/jupyter-book/blog/issues/new?template=blog-post.md) with as much as you can, and don't worry about getting it perfect.

## Write a blog post

Anybody is encouraged to write blog posts!

1. **Pick a topic.** Look in the [blog issues](https://github.com/jupyter-book/blog/issues?q=sort%3Aupdated-desc+is%3Aissue+is%3Aopen) for ideas, or bring your own.
2. **Add a markdown file** to `docs/posts/YYYY/`, where `YYYY` is the year you publish.
   If it's the first post of a new year, add a `posts/YYYY/*.md` pattern to the `toc` in [`docs/myst.yml`](docs/myst.yml).
   The file name becomes the end of the URL, so `docs/posts/2026/my-post.md` is published at `https://jupyterbook.org/blog/posts/2026/my-post`.
   Start the file with this metadata:

   ```yaml
   ---
   title: My post title
   date: 2026-01-31
   license: CC-BY-4.0
   authors:
     - id: jb-team # For team-wide posts like release notes, otherwise just use your name
   ---
   ```

   Author `id`s refer to entries in [`docs/authors.yml`](docs/authors.yml), so add yourself there if you're not listed yet.
   See the [MyST authorship guide](https://mystmd.org/guide/authorship) for other author fields, and browse `docs/posts/` for examples.
3. **Preview it** by following the [local development steps](README.md#local-development).
4. **Open a pull request** and ask for review in the [MyST Discord](https://discord.mystmd.org). Each pull request also gets a Netlify preview link.

## Writing style

- **Keep it short.** Aim for 300-500 words: what happened, why it matters, and where to learn more.
- **Write plainly.** Skip marketing language like "exciting", "powerful", or "seamless".
- **Link instead of explaining everything.** Point to docs, PRs, and issues for the details.
- **Add an image** or screenshot when it helps show what changed. Put it in `docs/posts/YYYY/images/`.
- **Put each sentence on its own line.** It makes pull request reviews easier.

## Write a release post

Release posts tell people what changed in a release and why they should care.[^1]
They usually cover `mystmd` and `myst-theme` (whose releases are tagged `myst-to-react@X.Y.Z`), and everything released since the last release post.
Name the file after the main release, like `docs/posts/2026/mystmd-1.11.0-release.md`.

[^1]: Release posts are not changelogs. Our changelogs are found in GitHub releases, and aggregated here: [jupyterbook.org/releases](https://jupyterbook.org/releases).

Write a release post when a release has something worth explaining, like a new feature or a change in behavior.
Routine bug-fix releases (usually patch releases) don't need a dedicated post.

For an example, see [the 1.11.0 release post](docs/posts/2026/mystmd-1.11.0-release.md).

### Structure

1. **Intro**: one or two sentences with any overall highlights or common themes in the release.
2. **What's new**: the highlights, split by audience if both are present:
   - **For authors**: people writing content with MyST or Jupyter Book.
   - **For developers building on MyST**: people building themes, templates, plugins, or tools that consume MyST.
3. **Changelogs**: link to [jupyterbook.org/releases](https://jupyterbook.org/releases) and the GitHub release notes.
4. **Upgrade notes**: `npm install -g mystmd` (or `pip install -U mystmd`) for `mystmd`. For `myst-theme`, delete `_build` and it downloads on the next build.
5. **Thank you contributors**: copy a unified contributor list from the GitHub release notes. Remove duplicates, bots, and AI agent accounts like `@claude`.

Format each highlight as a bold title followed by short sentences, one per line:

```md
- **Stable links to notebook cells**.
  Links to a notebook cell used to change on every build.
  MyST now [uses each cell's notebook ID as its anchor](https://github.com/jupyter-book/mystmd/pull/2975).
```

### Choosing what to include

- **Keep the bar high.** Aim for a handful of highlights, not every merged PR. Ask "would an author notice this, or would a developer need to act on it?" Group notable bug fixes into one "Bug fixes" item.
- **Leave out internal work.** Refactors, CI changes, dependency bumps, and docs about our own team processes belong in the changelog, not the post.
- **Be technically accurate.** Read the PR comments and implementation, not just its title, to ensure that our description is correct.
- **Say who it's for.** Make it clear if something is for authors or for developers building on MyST. If a feature isn't usable by authors yet, mention this in the notes.
- **Be specific.** "Run the MyST server on a custom host address" is better than "host customization".
- **Say why it is useful.** Clarify why each highlight is useful, the problem it is meant to solve, or the new functionality it's meant to enable.
- **Link words, not PR numbers.** Write `a new [children option](url)`, not `[#2705](url)`. Link each highlight to its documentation if it exists, and to the PR otherwise.
