"""Download and modify navigation items from jupyter-book site.yml."""
import urllib.request
import yaml


def process_urls(data):
    """Add https://jupyterbook.org/stable to URLs starting with /."""
    if isinstance(data, dict):
        return {
            k: f"https://jupyterbook.org/stable{v}" if k == "url" and isinstance(v, str) and v.startswith("/") else process_urls(v)
            for k, v in data.items()
        }
    elif isinstance(data, list):
        return [process_urls(item) for item in data]
    return data


url = "https://raw.githubusercontent.com/jupyter-book/jupyter-book/refs/heads/main/docs/_site/site.yml"
with urllib.request.urlopen(url) as response:
    data = yaml.safe_load(response)

with open("docs/site.yml", "w") as f:
    yaml.dump(process_urls(data), f, sort_keys=False)
