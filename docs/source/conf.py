# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Sioyek'
author = 'Ali Mostafavi'

release = '0.31'
version = '0.31.6'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.autosectionlabel',
]

autosectionlabel_prefix_document = True

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
