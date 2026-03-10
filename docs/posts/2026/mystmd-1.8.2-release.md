---
title: "What's new in mystmd 1.8.2"
date: 2026-03-10
license: CC-BY-4.0
authors:
  - id: jb-team
---

We've just released **mystmd 1.8.2** and a new version of the MyST react theme! Below are a few things that stand out.

## Interactive widgets with the `{anywidget}` directive

You can now [embed JavaScript widgets](https://mystmd.org/guide/widgets) in your MyST pages using the new `{anywidget}` directive. Widgets follow the [anywidget specification](https://anywidget.dev/), which gives plugin authors an extension point for embedding JS capabilities in their documents.

A widget is a JavaScript module that exports a `render` function. You pass it initial state as JSON in the directive body, and it renders an interactive element on the page. You could use this for interactive figures, explorable explanations, or custom visualizations without leaving MyST.

```{figure} ./images/anywidget-demo.png
:width: 400 
A little confetti demo that we use to show off embedding widgets in a MyST document with anywdiget!
```

:::{note}
Widget support is experimental. The interfaces may change as we learn more about usage patterns. Only load widgets from sources you trust, since they execute JavaScript in the reader's browser!
:::

## Table of contents improvements

The `{toc}` directive now supports a [`children` context option](https://github.com/jupyter-book/mystmd/pull/2705), which lets you display only the child pages of the current page rather than the full project table of contents. Use it on landing pages and index pages that introduce a section and link to its sub-pages. You can see an example in the [Jupyter Book getting started guide](https://jupyterbook.org/latest/get-started/).

## Better link handling across multi-site projects

If your project spans multiple domains (e.g., a docs site and a blog), you can now [configure a domain to be treated as "internal"](https://github.com/jupyter-book/myst-theme/pull/816) for link styling. Links to that domain will look like in-site navigation instead of external links. Check out [the Getting Started guide](https://jupyterbook.org/latest/get-started) for an example.

## Upgrade

To get the latest version of mystmd:

```bash
npm install -g mystmd
```

or for pip users:

```bash
pip install -U mystmd
```

The theme updates automatically. Delete your `_build` folder and mystmd will download the latest theme on your next build.

## Changelogs

Find an ongoing list of releases in the Jupyter Book ecosystem here:

[jupyterbook.org/releases](https://jupyterbook.org/releases)

You can also read the original [mystmd release notes](https://github.com/jupyter-book/mystmd/releases/tag/mystmd%401.8.2) and [myst-theme release notes](https://github.com/jupyter-book/myst-theme/releases/tag/myst-to-react%401.1.4).
