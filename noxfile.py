"""Nox sessions for Jupyter Book blog."""

import nox

# Use uv for faster installs
nox.options.default_venv_backend = "uv|virtualenv"

@nox.session(name="docs")
def docs(session):
    """Build the documentation as static HTML."""
    session.install("-r", "requirements.txt")
    session.chdir("docs")
    session.run("myst", "build", "--html", "--execute")


@nox.session(name="docs-live")
def docs_live(session):
    """Start a live development server for the documentation."""
    session.install("-r", "requirements.txt")
    session.chdir("docs")
    session.run("myst", "start", "--execute")


@nox.session
def clean(session):
    """Clean the documentation build artifacts."""
    session.install("-r", "requirements.txt")
    session.chdir("docs")
    session.run("myst", "clean", "-y")
