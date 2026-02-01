# The Jupyter Book blog

A blog for the Jupyter Book subproject.

## Repository layout

- `docs/` contains the blog itself as a MyST site.

## Local development

This blog is a small [MyST site](https://mystmd.org) with a blog plugin configured in `docs/myst.yml`.

To run it locally, take these steps:

1. **Install MyST** by [following the MyST installation instructions](https://mystmd.org/guide/installing).
2. **Build the site**:

   ```shell
   $ cd docs
   $ myst start
   ```

## Website deployment

The live site is built and deployed from `main` via `.github/workflows/deploy.yml`.
It is served at `blog.jupyterbook.org` and reverse-proxied at `jupyterbook.org/blog`.

## PR Previews

Netlify builds every pull request so previews are available for review (config in `netlify.toml`); previews are marked `noindex` and are not the live site.
