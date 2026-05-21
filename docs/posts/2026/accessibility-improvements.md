---
title: "New releases: improving accessibility in the myst theme"
date: 2026-05-21
license: CC-BY-4.0
authors:
  - id: jb-team
---

We've shipped new versions of `mystmd` and `myst-theme`!
A key part of this release was improving several [key ADA accessibility concerns](https://github.com/jupyter-book/mystmd/issues/2802) surfaced by an audit from [Silas](https://github.com/pancakereport) at UC Berkeley.
As part of this effort, we've also got a new accessibility statement for Jupyter Book and MyST:

- https://jupyterbook.org/accessibility
- https://mystmd.org/guide/accessibility-and-performance

Read below for some of the bigger improvements and fixes that we made.
Don't forget that accessibility bugs are treated like any other bug - please report accessibility issues!
We track them under the [`a11y` label in `myst-theme`](https://github.com/jupyter-book/myst-theme/labels/a11y) and in `mystmd`.

## Improvements we made

Most of the recent fixes landed in the default `myst-theme`s, which are the out-of-the-box web themes that come with mystmd and Jupyter Book:

- **Keyboard access for scrollable content.** Code blocks and cell outputs that scroll horizontally are now [focusable with the keyboard](https://github.com/jupyter-book/myst-theme/pull/849), [as are equations](https://github.com/jupyter-book/myst-theme/pull/860) and [text-based cell outputs](https://github.com/jupyter-book/myst-theme/pull/864).
- **Color contrast in terminal output.** The ANSI renderer for executed cell output now [supports a fuller color palette](https://github.com/jupyter-book/myst-theme/pull/857), and we [restricted the default palette](https://github.com/jupyter-book/myst-theme/pull/855) so colored text meets contrast requirements against both light and dark backgrounds.
- **Reflow at small viewports and high zoom.** [Wide tables no longer overflow the page](https://github.com/jupyter-book/myst-theme/pull/852), and the [navbar grows in height when content needs more room](https://github.com/jupyter-book/myst-theme/pull/863).
- **The search dialog is more screen-reader friendly.** We [improved ARIA semantics](https://github.com/jupyter-book/myst-theme/pull/854) on the "search popup" so screen readers announce it correctly.

We also shipped a user-facing change unrelated to accessibility!

- **Strict no longer force-checks links.** Strict mode now [skips link checking](https://github.com/jupyter-book/mystmd/pull/2819) so that it is faster and more reliable. This was causing a bunch of users to slow down their builds, but now you'll need to explicitly pass `--check-links` to ensure links are checked.

## Upgrade

Simply run `myst clean` or delete the `_build` folder and the next time you build with `myst` or `jupyter-book`, the new theme will be downloaded.
For the latest mystmd, you can run:

```bash
npm install -g mystmd
# or
pip install -U mystmd
```

## Acknowledgements

Full release notes are at [jupyterbook.org/releases](https://jupyterbook.org/releases).

Thanks to everyone who contributed discussions, ideas, code, and review across these releases:

[@agoose77](https://github.com/agoose77), [@bsipocz](https://github.com/bsipocz), [@choldgraf](https://github.com/choldgraf), [@engyrus](https://github.com/engyrus), [@fperez](https://github.com/fperez), [@FreekPols](https://github.com/FreekPols), [@JimMadge](https://github.com/JimMadge), [@kevinlin1](https://github.com/kevinlin1), [@mforbes](https://github.com/mforbes), [@pancakereport](https://github.com/pancakereport), [@Polirecyliente](https://github.com/Polirecyliente), [@rowanc1](https://github.com/rowanc1), [@ryanlovett](https://github.com/ryanlovett), [@stefanv](https://github.com/stefanv), [@stevejpurves](https://github.com/stevejpurves), [@TimMonko](https://github.com/TimMonko)
