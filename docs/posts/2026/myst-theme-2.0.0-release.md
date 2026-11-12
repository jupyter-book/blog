---
title: "New release: myst-theme 2.0 with an upgraded web stack, breadcrumbs, and redirects"
date: 2026-11-10
license: CC-BY-4.0
authors:
  - id: jb-team
---

We've just released [**myst-theme 2.0.0**](https://github.com/jupyter-book/myst-theme/releases/tag/myst-to-react%402.0.0)![^mystmd]
This brings in a full-upgrade of the infrastructure behind our web stack. It will make it more performant, easier to build into modern web applications, and easier to extend in the future.
It is incompatible with some older versions of mystmd, which is why this is a major release.
This release also comes with a few new features for authors, like breadcrumbs and redirects.

:::{important} You'll need mystmd `1.11.0` or newer
The new theme only works with **mystmd 1.11.0+** (or **Jupyter Book 2.1.7+**).
If you build with an older version, the build will show you an error.
You can either upgrade (see [](#upgrade-notes)), or pin to the old theme in your `myst.yml`:

```yaml
site:
  template: https://github.com/jupyter-book/myst-theme/releases/download/myst-to-react%401.4.1/book-theme.zip
```
:::

## For authors

- **Breadcrumbs in the book theme**.
  Pages now [show a breadcrumb trail](https://myst-theme.netlify.app/ui#breadcrumbs) above the title, like `🏠 › Visual Reference › Admonitions`.
  It follows the nesting of your table of contents, so readers can see where they are in the context of your book or documentation.
  You can turn it off with `site.options.hide_breadcrumbs: true`.

  ```{figure} ./images/myst-theme-2-breadcrumbs.png
  Breadcrumbs above the page title on the [myst-theme demo site](https://myst-theme.netlify.app/reference/admonitions).
  ```
- **Redirects for moved pages**.
  If you rename or move a page, you can now [redirect the old URL to the new one](https://myst-theme.netlify.app/permalinks#redirects) with `site.options.redirects`, so old links keep working (only in the book theme for now).
- **WebM videos**.
  The theme now [plays `.webm` files as videos](https://github.com/jupyter-book/myst-theme/pull/989).
- **Bug fixes**.
  Navbar links [now look like the other navbar items](https://github.com/jupyter-book/myst-theme/pull/964), and the mobile sidebar [can be dismissed on pages that use `hide_toc`](https://github.com/jupyter-book/myst-theme/pull/946).

## For developers building on MyST

- **The theme now uses React Router 8 and Vite**.
  We [upgraded the theme from Remix to React Router 8](https://github.com/jupyter-book/myst-theme/pull/972), the successor to Remix.
  This puts the theme on tooling that is more actively maintained, and should make it easier to build on.
  If you've customized or forked the theme, you may need to update your code!
- **Native static HTML builds**.
  The theme now [renders its own static HTML](https://github.com/jupyter-book/myst-theme/pull/961) using the render command added in [mystmd 1.11.0](https://github.com/jupyter-book/mystmd/releases/tag/mystmd%401.11.0) (previously, mystmd would start a server and crawl every page). This should be more efficient and reliable.
  The theme also [ships with its dependencies fully-bundled](https://github.com/jupyter-book/myst-theme/pull/970), so it no longer needs to install dependencies on your machine.
- **Multi-project sites are no longer supported**.
  The 2.0 theme [drops support for sites made of multiple projects](https://github.com/jupyter-book/myst-theme/pull/970). These have been [deprecated for some time](https://github.com/jupyter-book/mystmd/issues/2886#issuecomment-4596054417), and this removes multi-project logic from the theme.

## Changelogs

You can also read about this release at [jupyterbook.org/releases](https://jupyterbook.org/releases).
For more details, see the [myst-theme release notes](https://github.com/jupyter-book/myst-theme/releases/tag/myst-to-react%402.0.0).

(upgrade-notes)=
## Upgrade notes

Upgrade `mystmd` or `jupyter-book` first, then delete `_build` so the new theme is downloaded on your next build.

::::{tab-set}
:::{tab-item} mystmd (npm)
```bash
npm install -g mystmd
```
:::
:::{tab-item} mystmd (pip)
```bash
pip install -U mystmd
```
:::
:::{tab-item} Jupyter Book
```bash
pip install -U jupyter-book
```
:::
:::{tab-item} myst-theme
Remove the build folder and it'll automatically download the latest theme the next time you build your site:

```bash
rm -rf _build
```
:::
::::

## Try it out!

This is a big change under the hood, so we'd love your feedback!
Try the new release and [open an issue](https://github.com/jupyter-book/myst-theme/issues) if something breaks.

## Thank you contributors!

This release would not have been possible without the help of our community!
Thanks to everyone who contributed discussions, ideas, code, and review across this release:
[@agoose77](https://github.com/agoose77),
[@choldgraf](https://github.com/choldgraf),
[@goekce](https://github.com/goekce),
[@pancakereport](https://github.com/pancakereport),
[@rowanc1](https://github.com/rowanc1), and
[@stefanv](https://github.com/stefanv).

[^mystmd]: We also recently released [mystmd 1.12.0](https://github.com/jupyter-book/mystmd/releases/tag/mystmd%401.12.0), which adds `--execute-parallel` to `myst start`, finer-grained `error_rules`, and support for `.webm` and `.avif` files. It also requires Node 22 or newer.
