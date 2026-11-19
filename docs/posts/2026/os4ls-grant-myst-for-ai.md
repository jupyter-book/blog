---
title: Our submission to OS for Life Sciences 2026, "Making MyST the documentation engine for AI-era bioscience"
date: "2026-11-17"
license: CC-BY-4.0
authors:
  - sbonaretti
  - jb-team
---

Last July, we submitted a full proposal to [Open Source for the Life Sciences](https://os4science.org/funding_opportunity/os4ls/), a program of [Renaissance Philanthropy](https://www.renaissancephilanthropy.org/).
Unfortunately, our proposal was not selected for funding. 
However, we decided to share it in case others are interested in learning more about our vision for MyST in the AI-era of bioscience, or wish to explore other ways to bring some of these ideas to life.

The full proposal is on Zenodo (https://doi.org/10.5281/zenodo.24350888).
Below, we share the summary of the proposal.


## Making MyST the documentation engine for AI-era bioscience (Summary)  

LLMs have expanded the ways in which researchers learn about and use open source infrastructure. Instead of learning about tools with a search engine and following instructions, researchers can use a Large Language Model (LLM) to generate code for their analysis and communicate that work with others. As the scientific community increasingly relies on LLMs, it is crucial that the tools scientists use for communication also provide a structured, machine-readable foundation that LLMs can leverage to accelerate learning and discovery.

MyST ([mystmd.org](http://mystmd.org)) is a documentation engine developed by the Jupyter Book subproject of Project Jupyter ([jupyter.org](http://jupyter.org)). It is the engine behind Jupyter Book ([jupyterbook.org](http://jupyterbook.org)), which powers over 18,000 publicly available books, courses, and knowledge bases. MyST has an excellent foundation for LLMs because its content is structured data by design: every MyST document includes a machine-readable JSON file to encourage re-use, interoperability, and discoverability. While most documentation “in the wild” is unstructured text (requiring an LLM to scrape and infer context from messy data), MyST content is designed to be read, traversed, and re-used programmatically.

With strategically-targeted improvements to MyST’s extensibility and plugin API, and by natively integrating it with core workflows in the Jupyter ecosystem, there’s an opportunity to position MyST and Jupyter as the premier open communication engine for computational narratives in the age of LLMs. By expanding the capabilities of MyST’s plugin architecture, we can leverage the power of LLMs to rapidly build on top of APIs to extend MyST in new directions. By integrating MyST as a first-class citizen in Jupyter workflows, we can meet scientists where they are by integrating MyST into the core Jupyter workflows they already use, and providing text-native workflows with Jupyter Notebooks.
