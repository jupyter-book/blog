---
title: Jupyter Book Becomes a Jupyter Subproject
subtitle: Jupyter Book joins the ranks of other Jupyter Subprojects such as JupyterLab and JupyterHub.
date: 2024-11-11
license: CC-BY-4.0
---

Over the last ten months, the Jupyter Book team have been hard at work building the next major version of Jupyter Book (see [the blog post][plan]). During this time, a strong distinction between the tools developed for the legacy Sphinx application and its new [MyST Engine][mystmd]-powered sibling has arisen, leading to the submission of a [Jupyter Enhancement Proposal to incorporate Jupyter Book][book-jep] as a Jupyter Subproject.

Under the Jupyter organisation, the Jupyter Book team hopes to have found

> a longer-lasting and organizationally-neutral home for the vision, strategy, tools, and standards of this modern version of the Jupyter Book toolchain.
>
> -- [Jupyter Enhancement Proposal #122](https://github.com/jupyter/enhancement-proposals/pull/123)

To facilitate the creation of a Jupyter Subproject, a [new `jupyter-book` GitHub Organisation][jbp] has been created. This new organisation is distinct from the [Executable Books organisation][ebp] that served as the home for previous releases of Jupyter Book; It will act as the hub for all future development and discussion surrounding Jupyter Book development.

For more news about Jupyter Book, such as the upcoming Jupyter Book 2 alpha release, please keep an eye on this blog!

[jbp]: https://github.com/jupyter-book
[ebp]: https://github.com/executablebooks
[plan]: https://executablebooks.org/en/latest/blog/2024-05-20-jupyter-book-myst/
[book-jep]: https://github.com/jupyter/enhancement-proposals/pull/123
[mystmd]: https://mystmd.org
