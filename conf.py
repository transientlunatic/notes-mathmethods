import sphinx_daniel_theme

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Mathematics for Physics'
copyright = '2020, Daniel Williams'
author = 'Daniel Williams'

# The full version, including alpha/beta/rc tags
release = 'v0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.imgconverter',
              'sphinxcontrib.bibtex',
              'sphinxcontrib.tikz',
              'sphinxcontrib.thm']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = 'daniel'
html_theme_path = sphinx_daniel_theme.get_html_theme_path()

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
mathjax_config = {
    "loader": {
        "load": ['[tex]/physics', '[siunitx]/siunitx.js'],
        "paths": {'siunitx': 'http://rawgit.com/burnpanck/MathJax-siunitx/master/'}
    },
    "tex": {
        "packages": {'[+]': ['physics', 'siuntix']},
        "macros": {
            "div": r"\nabla",
            "ld": [r"\unicode{xA3}_{#1}{#2}", 2],
            "rn": "\mathbb{R}",
            "dinf": "\mathrm{d}",
            "dd": ["\,\dinf #1", 1],
            "of": [r'\tilde{#1}', 1],
            "ten": [r'\mathsf{{#1}}', 1],
            "RR": '{\\bf R}',       
            "bold": ['{\\bf #1}',1] 
            }                       
        }                           
    }                               


latex_elements = {
 'preamble': r'''
     % make phantomsection empty inside figures
     \usepackage{etoolbox}
     \AtBeginEnvironment{figure}{\renewcommand{\phantomsection}{}}
 '''
}
