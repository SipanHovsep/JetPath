import os, sys
sys.path.insert(0, os.path.abspath(".."))  # so autodoc sees your packages

project = "JetPath"
extensions = [
    "myst_parser",        # Markdown + MyST
    "myst_nb",            # render notebooks (.ipynb/.md)
    "sphinx.ext.autodoc", # API docs from docstrings
    "sphinx.ext.napoleon",# Google/NumPy docstrings
    "sphinx.ext.autosectionlabel",
]
myst_enable_extensions = ["colon_fence", "linkify"]
nb_execution_mode = "off"  # build quickly without executing notebooks
html_theme = "furo"
html_title = "JetPath Docs"
