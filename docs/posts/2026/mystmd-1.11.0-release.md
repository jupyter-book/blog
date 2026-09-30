---
title: "New release: stable notebook cell links, figure grids, and new hooks for theme developers"
date: 2026-09-24
license: CC-BY-4.0
authors:
  - id: jb-team
---

We've just released [**mystmd 1.11.0**](https://github.com/jupyter-book/mystmd/releases/tag/mystmd%401.11.0) and [**myst-theme 1.4.1**](https://github.com/jupyter-book/myst-theme/releases/tag/myst-to-react%401.4.1)!
Here are some of the bigger improvements and fixes that we made.

## For authors

- **Stable links to notebook cells**.
  Links to a notebook cell (like `page#cell-id`) used to change on every build.
  MyST now [uses each cell's notebook ID as its anchor](https://github.com/jupyter-book/mystmd/pull/2975), and the theme [supports Jupyter-style `#cell-id=<id>` links](https://github.com/jupyter-book/myst-theme/pull/915), so links to cells keep working across builds.
- **Grid layouts inside figures**.
  You can now [put a `{grid}` inside a `{figure}`](https://mystmd.org/guide/figures#control-sub-figure-layout-with-a-grid) for responsive multi-image layouts, like one column on narrow screens and two on wide ones.
- **Fewer surprise DOI citations**.
  MyST used to turn any link that ended in a DOI into a citation.
  Now, [only `doi.org` links are converted](https://github.com/jupyter-book/mystmd/pull/2960), along with raw DOIs and `doi:` links.
  To keep the old behavior, set [`infer_dois_from_urls: true`](https://mystmd.org/guide/settings#setting-infer-dois-from-urls).
- **Execution cache stored as notebooks**.
  MyST now [stores cached execution outputs as `.ipynb` files](https://github.com/jupyter-book/mystmd/pull/2970).
  If you're debugging a build, you can inspect cached outputs with any notebook viewer.
  Existing caches still work.
- **Serve `myst start` on your network**.
  We've documented how to [run the MyST server on a custom host address](https://mystmd.org/guide/deployment#serving-on-a-network-interface), for example from a container or a remote machine.
- **Bug fixes**.
  Figures made from captioned notebook cells [show their images again](https://github.com/jupyter-book/mystmd/pull/3059) (this broke in mystmd 1.7.0).
  Multi-word glossary terms [no longer break Typst PDF export](https://github.com/jupyter-book/mystmd/pull/3047).
  On Windows, notebooks now [execute from their own folder](https://github.com/jupyter-book/mystmd/pull/3023), so relative file paths work.

## For developers building on MyST

These changes are for people building themes, templates, or other tools on top of MyST.
They don't change anything for authors yet.

- **A new HTML rendering pathway for themes**.
  A theme can now [declare its own render command](https://github.com/jupyter-book/mystmd/pull/3027) for `myst build --html`.
  If it does, `mystmd` runs that command instead of starting a server and crawling every page, so a theme could use a static site generator approach.
- **A manifest of public files**.
  Site builds now [include a `public.json` file](https://github.com/jupyter-book/mystmd/pull/3002) that lists the files under `public/`, so themes can build static sites without file-system access to the site content.
- **New developer documentation**.
  We added a guide to [the MyST AST structure and metadata](https://github.com/jupyter-book/mystmd/pull/2865) and documented how a plugin can [aggregate information across multiple pages](https://github.com/jupyter-book/mystmd/pull/2950), like a site-wide glossary.

## Changelogs

You can also read about this release at [jupyterbook.org/releases](https://jupyterbook.org/releases).
For more details, see
[mystmd release notes](https://github.com/jupyter-book/mystmd/releases/tag/mystmd%401.11.0)
and
[myst-theme release notes](https://github.com/jupyter-book/myst-theme/releases/tag/myst-to-react%401.4.1).

## Upgrade notes

- To upgrade `mystmd`:
    `npm install -g mystmd` (or `pip install -U mystmd`)

- To upgrade `myst-theme`:
     Delete `_build`; it will be downloaded again during the next build.

## Try it out!

We'd love your feedback! Try the new release and let us know what works well and where we can improve.

## Thank you contributors!

This release would not have been possible without the help of our community!
Thanks to everyone who contributed discussions, ideas, code, and review across this release:
[@agoose77](https://github.com/agoose77),
[@bsipocz](https://github.com/bsipocz),
[@choldgraf](https://github.com/choldgraf),
[@ciyer](https://github.com/ciyer),
[@coretl](https://github.com/coretl),
[@Darshan808](https://github.com/Darshan808),
[@DobbiKov](https://github.com/DobbiKov),
[@dylanpulver](https://github.com/dylanpulver),
[@FernandoBasso](https://github.com/FernandoBasso),
[@fperez](https://github.com/fperez),
[@FreekPols](https://github.com/FreekPols),
[@fwkoch](https://github.com/fwkoch),
[@humitos](https://github.com/humitos),
[@jasongrout](https://github.com/jasongrout),
[@JimMadge](https://github.com/JimMadge),
[@Jorge-Polanco-Roque](https://github.com/Jorge-Polanco-Roque),
[@KirstieJane](https://github.com/KirstieJane),
[@kmuehlbauer](https://github.com/kmuehlbauer),
[@krassowski](https://github.com/krassowski),
[@mfisher87](https://github.com/mfisher87),
[@Montanajim](https://github.com/Montanajim),
[@nocomplexity](https://github.com/nocomplexity),
[@parmentelat](https://github.com/parmentelat),
[@rowanc1](https://github.com/rowanc1),
[@sbonaretti](https://github.com/sbonaretti),
[@sinclairtarget](https://github.com/sinclairtarget),
[@stefanv](https://github.com/stefanv),
[@stevejpurves](https://github.com/stevejpurves), and
[@TimMonko](https://github.com/TimMonko).
