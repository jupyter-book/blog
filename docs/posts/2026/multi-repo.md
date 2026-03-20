---
title: "How we combine multiple repositories into one website at jupyterbook.org"
date: 2026-03-10
license: CC-BY-4.0
authors:
  - id: choldgraf
---

The Jupyter Book project has content in a bunch of different repositories - [user docs](https://github.com/jupyter-book/jupyter-book), [a blog](https://github.com/jupyter-book/blog), [a team compass](https://github.com/jupyter-book/team-compass), and [project & community pages](https://github.com/jupyter-book/jupyterbook.org). We recently finished an initiative to serve each set of content at `jupyterbook.org`, while keeping the source files separated in their repositories.

Getting there required a combination of Netlify configuration and several improvements to MyST and the MyST theme along the way. This post walks through the pieces and how they fit together, so you can do something similar with a multi-repo project.

## Why is this useful?

Two things bugged us about the old setup:

1. We had multiple types of content embedded in one repository. In particular we had **versioned user documentation** alongside **evergreen community documentation** (e.g., [the roadmaps page](https://jupyterbook.org/roadmap)). This meant we had duplicated content for some user documentation, and a slow lag time before it'd make it's way into `/stable`.
2. Search engines treat subdomains as separate websites, so `blog.jupyterbook.org` wasn't helping `jupyterbook.org` in search rankings.

We wanted `jupyterbook.org`, `jupyterbook.org/blog`, `jupyterbook.org/stable`, `jupyterbook.org/compass` all under one roof, with each repo still deploying on its own via static websites.

We accomplished this with **Netlify proxy rules** and **shared MyST configuration**!

## Proxying sub-sites with Netlify rewrites

We discovered that [Netlify reverse proxy rules](https://docs.netlify.com/routing/redirects/rewrites-proxies/) are a great way to accomplish this. These essentially intercept queries to a URL path (eg. `/blog/**`) and serve content at that path from elsewhere (e.g., `blog.jupyterbook.org`). The browser sees `jupyterbook.org/blog`, but Netlify fetches the content from a totally different site behind the scenes.

We set up a ["jupyterbook.org" repo](https://github.com/jupyter-book/jupyterbook.org) that serves the landing page and our evergreen community documentation, and proxies everything else:

- `/` - served directly from the [jupyterbook.org repo](https://github.com/jupyter-book/jupyterbook.org) (served on Netlify)
- `/blog` - proxied from the [blog repo](https://github.com/jupyter-book/blog) (served on Netlify)
- `/compass` - proxied from the [team-compass repo](https://github.com/jupyter-book/team-compass) (Served on Netlify)
- `/stable` - proxied from the [jupyter-book repo](https://github.com/jupyter-book/jupyter-book) (served on [ReadTheDocs](https://readthedocs.org))

Here's what the [`netlify.toml`](https://github.com/jupyter-book/jupyterbook.org/blob/main/netlify.toml) looks like (simplified):

```{code} toml
:filename: netlify.toml
# Blog: proxied from another Netlify site
[[redirects]]
  from = "/blog/*"
  to = "https://jupyter-book-blog.netlify.app/blog/:splat"
  status = 200
  force = true

# User docs: proxied from ReadTheDocs
[[redirects]]
  from = "/stable/*"
  to = "https://jupyter-book.readthedocs.io/stable/:splat"
  status = 200
  force = true
```

Each repo deploys independently, meaning we can update the content at whatever cadence is best for that repository. The jupyterbook.org repo only needs updating when the nav structure changes. But making it all *feel* like one site took some work on the MyST side.

## Shared configuration with `extends`

MyST's [`extends:` configuration](https://mystmd.org/guide/external-references) lets one project inherit configuration from another. We use this to share navbar, logo, and favicon config across all sub-sites from a single [`site.yml`](https://github.com/jupyter-book/jupyterbook.org/blob/main/docs/_site/site.yml) in the core repo:

```yaml
# In the blog's myst.yml
extends:
  - https://github.com/jupyter-book/jupyterbook.org/raw/refs/heads/main/docs/_site/site.yml
```

If we change the configuration at that file, it'll automatically be inherited in every other repository when we re-build it (usually done on each commit, or on a daily CRON job with GitHub Actions).

Here are a few useful things that we've shared across sites via the pattern above:

- Navigation bar URLs
- Site footer configuration
- Site branding (logo, titles, etc)
- Announcement bars (when we need a temporary announcement to show up everywhere)
- Internal domain configuration (see above)

Along the way we [added `parts:` support to the `extends:` key](https://github.com/jupyter-book/mystmd/issues/2126) to get this working.


## One gotcha: `BASE_URL` for asset paths

MyST bakes `BASE_URL` into CSS, JS, and image paths at build time. If you build with `BASE_URL=/` but serve at `/blog`, none of those load properly.

To fix this, each sub-site builds with `BASE_URL` set to its final path on jupyterbook.org. For example, here's some [Netlify config](https://github.com/jupyter-book/blog/blob/main/netlify.toml) from the blog that does this:

```toml
[build]
  publish = "publish"
  # This ensures that `/blog` is appended to asset paths
  environment = { BASE_URL = "/blog" }
  command = """
    cd docs && myst build --html && \
    mkdir -p ../publish/blog && \
    # Here we move the HTML assets to the blog
    mv _build/html/* ../publish/blog/
  """
```

## `internal_domains` for cross-site navigation

`BASE_URL` fixes asset loading, but it doesn't fix navigation. Jupyter Book used to treat full URLs as "external" links, adding an extra icon and opening a new tab when clicked. This led to a bunch of tabs any time you navigated around jupyterbook.org, and was [also reported by the Project Pythia team](https://github.com/jupyter-book/mystmd/issues/2719).

We added an [`internal_domains` option](https://github.com/jupyter-book/myst-theme/pull/816) to fix this:

```yaml
site:
  options:
    internal_domains: jupyterbook.org
```

Now the theme treats any link to `jupyterbook.org` as internal. It provides same-tab navigation and no external link icon, even though the link is technically a full URL.

## Want to do this too?

Hopefully this is a useful workflow for communities that have multiple repositories of content. 

All of the config is in [jupyter-book/jupyterbook.org](https://github.com/jupyter-book/jupyterbook.org), and the tracking issue with the full story is [jupyter-book/jupyter-book#2528](https://github.com/jupyter-book/jupyter-book/issues/2528).

If you've got questions about this work, come chat with us at [discord.mystmd.org](https://discord.mystmd.org).

## Acknowledgements

- Thanks to [Project Pythia](https://projectpythia.org/) for providing additional guidance, collaboration, and support for this work.
- Thanks to [EarthScope](https://docs.earthscope.org/en/latest/intro.html) for giving user feedback about the usefulness of this as they explore converting their docs to the new MyST engine.
