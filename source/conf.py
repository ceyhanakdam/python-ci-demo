# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys
# Add the project root (one level up from 'source/') to the path so Sphinx can find 'my_package'
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'My Python Package'
copyright = '2025, Ceyhan Akdam'
author = 'Ceyhan Akdam'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',     # Required to read docstrings from Python code
    'sphinx_rtd_theme',       # Required for the Read the Docs theme
]

templates_path = ['_templates']
exclude_patterns = []

language = 'en' # Changed to 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme' # Changed to use the 'Read the Docs' theme
html_static_path = ['_static']