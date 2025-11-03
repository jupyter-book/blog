---
title: "Why we made a major release for Jupyter Book 2 instead of creating a new package"
date: 2025-11-03
license: CC-BY-4.0
authors:
  - Jupyter Book Team
---

Last night, we [released Jupyter Book 2](https://github.com/jupyter-book/jupyter-book/releases/tag/v2.0.0). This is a major release that introduces the [MyST Document Engine](https://mystmd.org) as the back-end infrastructure that powers Jupyter Book.

It also means that many Jupyter Books out there are now broken! In particular, users who haven't pinned their Jupyter Book versions to the `1.x` series will likely have an unexpected surprise. Users can pin their version of Jupyter Book with commands like so:

```shell
$ pip install "jupyter-book<2"
OR
$ pip install "jupyter-book~=1"
```

However we know that many people do not do this in practice.

## Why we didn't create an entirely new package

We considered creating a new Python package to reflect this big switch - e.g., `pip install jupyter-book2`. This has been done before in the Python system, and is a way to strictly separate the two projects.

However, we also feel that this introduces a lot of confusion for users, and introduces an unsustainable maintenance burden for developers. Maintaining two user-facing products simultaneously creates expectations that we can't meet, and dilutes the brand and product identity of the tool.

For this reason, we opted to make a major release (`pip install jupyter-book`) instead of creating a new package (`pip install jupyter-book2`).

## What we're doing to help

We know that this will result in hidden breakages in CI/CD and unexpected changes to user workflows.
We are sorry about this! We know that it's a huge pain to have to update your infrastructure and debug unexpected changes. Here are recommended paths forward:

(downgrade-jb1)=
### Downgrade to Jupyter Book 1

The simplest thing that you could do is to simply _downgrade to Jupyter Book 1_.
It is still available, and you can downgrade from the command-line like so:

```shell
$ pip install "jupyter-book<2"
```

Or via a file like `requirements.txt` like so:

```{code-block}
:filename: requirements.txt
jupyter-book<2
```

This will keep the previous version of Jupyter Book installed.

### Use the upgrade guide and helper

We've also created an [upgrade guide for Jupyter Book 1](xref:jb#upgrade-tldr) to help people navigate their upgrade path. This includes guides to translate "old" configuration (`_config.yml`) to "new" configuration (`myst.yml`) and several paper-cuts along the way.

Bundled with this effort is an **auto-upgrade tool** that will try and do most of the hard work for you. If you run `jupyter book build` in a directory with "old style" configuration, it should prompt you to automatically upgrade your book's configuration.

We hope that these reduce the burden on users in upgrading their books if they wish, but we want to re-iterate that users don't strictly need to upgrade! You can always [downgrade to Jupyter Book 1](#downgrade-jb1) and keep using that.

### Ask for support and guidance in our community channels

Finally, we've set up a number of [community channels](jb:community) where users and project contributors can discuss with one another and ask questions. Here are a few dedicated spaces:

Here are a few helpful links if you'd like to learn more:

- [Our chat room](https://discord.mystmd.org/) is for quick conversations and synchronous questions.
- [Our discussions forum](https://github.com/orgs/jupyter-book/discussions) is for all kinds of general questions.
- The [Upgrading Jupyter Book category](https://github.com/orgs/jupyter-book/discussions/categories/upgrading-jupyterbook) is a special section of the forum for asking questions about upgrades.

The Jupyter Book team will be monitoring these channels for questions from folks as they hit papercuts and snags while they upgrade.

## Thanks for your support

Thanks again for using Jupyter Book and being part of our community. We know that disruptions to your workflow are really annoying! We're sorry if this decision has made your day more difficult. We're confident this is the right decision, and are committed to helping, guiding, and learning with our community to make the transition as smooth as possible.
