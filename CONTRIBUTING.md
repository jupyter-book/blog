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

Anybody is encouraged to share blog post ideas! Here are some tips:

- Fill out the [blog post issue template](https://github.com/jupyter-book/blog/issues/new?template=blog-post.md)
- Fill in as much as you can but don't worry about getting it perfect!

## Write a blog post

Anybody is encouraged to write blog posts! Here are some tips:

- Look in the [issues for our blog](https://github.com/jupyter-book/blog/issues?q=sort%3Aupdated-desc+is%3Aissue+is%3Aopen) for things you could blog about
- Feel free to blog about any of them!
- Do so by adding a new markdown file to the folder `posts/current-year`, where `current-year` is the year in which the post is published
  - Make sure to include at least the following metadata at the top of your markdown file:
    ```
    ---
    title: 
    date: 
    authors:
      - 
    ---
    ```
    You can find detailed information about the metadata in the [MyST authorship guide](https://mystmd.org/guide/authorship). For examples, browse the files in the `posts/` directory.

  - Choose a descriptive file name, as it will become the last part of the page URL. For example, a file named `my-post.md` will be accessible at `https://jupyterbook.org/blog/posts/current-year/my-post`  
- Make a Pull Request and ping the team for review and editing in Discord

## Write a release post

Release posts tell people what changed in a release and why they should care.[^1]

[^1]: Releases are not changelogs - our changelogs are found in GitHub releases, and aggregated here: [jupyterbook.org/releases](https://jupyterbook.org/releases).

Write a release post when a release has something worth explaining, like a new feature or a change in behavior.
Routine bug-fix releases (usually patch releases) don't need a dedicated post.

For examples, see [the 1.11.0 release post](docs/posts/2026/mystmd-1.11.0-release.md) and [the 1.8.2 release post](docs/posts/2026/mystmd-1.8.2-release.md).

### Structure

1. **Intro**: one or two sentences with any overall highlights or common themes in the release.
2. **What's new**: the highlights, split by audience if both are present:
   - **For authors**: people writing content with MyST or Jupyter Book.
   - **For developers building on MyST**: people building themes, templates, plugins, or tools that consume MyST.
3. **Changelogs**: link to [jupyterbook.org/releases](https://jupyterbook.org/releases) and the GitHub release notes.
4. **Upgrade notes**: how to upgrade each package that was released.
5. **Thank you contributors**: copy a unified contributor list from the GitHub release notes. Make sure to remove any duplicated entries and bots.

Format each highlight as a bold title followed by short sentences, one per line. Ensure you link the PR that enabled this in the text:

```md
- **Stable links to notebook cells**.
  Links to a notebook cell used to change on every build.
  MyST now [uses each cell's notebook ID as its anchor](https://github.com/jupyter-book/mystmd/pull/2975).
```

### Choosing what to include

- **Keep the bar high.** Aim for a handful of highlights, not every merged PR. Ask "would an author notice this, or would a developer need to act on it?"
- **Leave out internal work.** Refactors, CI changes, dependency bumps, and docs about our own team processes belong in the changelog, not the post.
- **Be technically accurate.** Read the PR comments and implementation, not just its title, to ensure that our description is correct.
- **Say who it's for.** Make it clear if something is for authors or for developers building on MyST. If a feature isn't usable by authors yet, mention this in the notes.
- **Be specific.** "Run the MyST server on a custom host address" is better than "host customization".
- **Say why it is useful.** Clarify why each highlight is useful, the problem it is meant to solve, or the new functionality it's meant to enable.
- **Link words, not PR numbers.** Write `a new [children option](url)`, not `[#2705](url)`. Link to documentation when it exists.
