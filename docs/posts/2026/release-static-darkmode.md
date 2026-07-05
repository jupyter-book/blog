---
title: "New release: More reliable static content, dark mode improvements, and more!"
date: 2026-07-06
license: CC-BY-4.0
authors:
  - id: jb-team
---

We're pleased to announce the latest releases of `mystmd` (v1.10.1) and `myst-theme` (v1.3.1).
We improved the static asset resolution, the dark mode experience, and the theme experience among others. 
Read below for some of the bigger improvements and fixes that we made!


## What's new

- **Improved Support for Static Content**. One of the most important updates in this release is [improved handling of project static files across the MyST ecosystem](https://github.com/jupyter-book/myst-theme/pull/887). 
When the theme encounters a route that does not resolve to a MyST page, it now checks the content server to determine whether the requested path corresponds to a static asset. 
If a matching file is found, the request is redirected and served directly by the content server.
Alongside this work, we've expanded the [documentation around static file behavior](https://github.com/jupyter-book/myst-theme/pull/892) to make it easier for users and contributors.

- **Better Dark Mode Experience**. 
Dark mode continues to be an important part of the reading experience for many users. 
This release improves [compatibility with Mermaid diagrams](https://github.com/jupyter-book/myst-theme/pull/881) when dark mode is enabled, ensuring that diagrams remain readable and visually consistent across themes. 
We have also refined theme behavior by [improving logo rendering in dark mode](https://github.com/jupyter-book/myst-theme/pull/876).

- **Other theme improvements.**
This release includes several refinements to the user interface that help create a smoother and more polished experience for readers. 
Among others, we have improve theme behavior by [preventing unnecessary theme-transition animations](https://github.com/jupyter-book/myst-theme/pull/884), reducing visual distractions and making transitions feel more natural. 
We also [fixed vertical height for stacked buttons](https://github.com/jupyter-book/myst-theme/pull/872), ensuring that interactive elements display consistently.


## Changelogs
You can also read about this release at [jupyterbook.org/releases](https://jupyterbook.org/releases). 
For more details, see
[mystmd release notes](https://github.com/jupyter-book/mystmd/releases/tag/mystmd%401.10.1) 
and 
[myst-theme release notes](https://github.com/jupyter-book/myst-theme/releases/tag/myst-to-react%401.3.1).


## Upgrade notes
<!-- Choose what needed -->

- To upgrade `mystmd`:   
    `npm install -g mystmd` (or `pip install -U mystmd`)

- To upgrade `myst-theme`:   
     Delete `_build` and it downloads on the next build



## Try it out!
We'd love your feedback. Try the new release and let us know what works well and where we can improve.


## Thank you contributors!
This release would not have been possible without the help of our community.
Thanks to everyone who contributed discussions, ideas, code, and review across this release, especially:
[@agoose77](https://github.com/agoose77), 
[@chad-earthscope](https://github.com/chad-earthscope),
[@choldgraf](https://github.com/choldgraf), 
[@joequant](https://github.com/joequant),
[@pancakereport](https://github.com/pancakereport), 
[parmentelat](https://github.com/parmentelat),
[@rowanc1](https://github.com/rowanc1),
[@stefanv](https://github.com/stefanv), and
[@stevejpurves](https://github.com/stevejpurves). 