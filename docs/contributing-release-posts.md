---
title: "Writing a release blog post"
date: 2026-06-05
---

A "release post" tells readers what changed in a recent `mystmd` or `myst-theme` release, why it matters, and how to upgrade.
This is a short guide for how to write one.

:::{note} Some examples
For examples, read [What's new in mystmd 1.8.2](./posts/2026/mystmd-1.8.2-release.md) and [improving accessibility in the myst theme](./posts/2026/accessibility-improvements.md).
:::

## Where release information lives

There are three sources, in increasing order of detail:

- **[jupyterbook.org/releases](https://jupyterbook.org/releases)** is the aggregated changelog across the ecosystem. Start here to see what's shipped recently.
- **GitHub release notes** hold the auto-generated, PR-by-PR changelog for each repo: [mystmd releases](https://github.com/jupyter-book/mystmd/releases) and [myst-theme releases](https://github.com/jupyter-book/myst-theme/releases).
- **The PRs and issues** themselves often have extra context for why a change was made, challenges we ran into, etc. Follow the links in the release notes to understand a feature well enough to describe it.

## Choose what to write about

Choose a few things that are worth highlighting in the post.
You don't need to mention everything! Usually just 1-3 things is enough.
**Focus on user-facing changes**, for example:

- New features or directives (e.g. the `{anywidget}` directive)
- Changes to how something already works (e.g. strict mode no longer checking links)
- Notable bug fixes, especially ones people hit often
- Important usability improvements for certain groups of users (e.g. accessibility)
- Milestones worth celebrating (a big accessibility pass, a major version)

:::{warning} Confirm that a Jupyter Book release has been made if `mystmd` was released
Jupyter Book needs its own release after `mystmd` releases a new version in order for Jupyter Book users to get the changes.
Double check that we've done this before writing about it, otherwise JB users won't be able to use any of these improvements!
For theme upgrades, it shouldn't be a problem because those get re-downloaded when the `_build` folder is deleted.
:::

## Structure the post

Aim for **300-400 words**. A good post:

1. **Lead** with one or two sentences on what shipped overall, and why a reader should care. If there was any broad theme for these changes (e.g. "A bunch of accessibility improvements" note it here).
2. **Highlight 2-3 standout changes**, each with a short `## heading`. Describe what it does and why it's useful. Link to the docs to learn more, and to the most-relevant PR where the work happened.
3. **Add an "Upgrade" section** with install instructions:
   - `mystmd`: `npm install -g mystmd` (or `pip install -U mystmd`)
   - `myst-theme`: delete `_build` and it downloads on the next build
   - `jupyter-book`: `pip install -U jupyter-book`
4. **Ends with a "Changelogs" section** pointing to [jupyterbook.org/releases](https://jupyterbook.org/releases) and the individual GitHub release pages.
5. **Thank contributors** where it fits - link the GitHub handles for contributors, which should auto-link their handle.

A few style notes that keep posts readable:

- Link PRs on words in a sentence, not as bare numbers. Write `` a new [`children` option](link) ``, not `[#2705](link)`.
- Keep the tone direct and friendly: "you can now...", "we've shipped...".
- Put a line break after each sentence in the source, which keeps diffs clean.

## Commit, PR, and review

1. Add your file to `docs/posts/<year>/<slug>.md` and name it with a descriptive slug.
2. Build locally to check it renders: `nox -s docs-live`.
3. Open a pull request against `main`. Netlify builds a preview on every PR, so reviewers can read the rendered post.
4. Ping the team in Discord for review and editing.

The live site deploys from `main` automatically once the PR merges.
