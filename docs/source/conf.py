# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Make the pydblite package importable for autodoc.
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------

project = 'PyDbLite'
copyright = '2009-2026, Pierre Quentel, Bendik Rønning Opstad, Viacheslav Vic Bukhantsov'
author = 'Pierre Quentel, Bendik Rønning Opstad, Viacheslav Vic Bukhantsov'

# The version info is fetched from the installed package.
try:
    import pydblite
    version = release = pydblite.__version__
    print("Building docs for pydblite v%s" % version)
except Exception as e:  # pragma: no cover
    print("Failed to find pydblite version:", e)
    version = release = ''

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
]

source_suffix = '.rst'
master_doc = 'index'
language = 'en'

# Fragments that are included into other documents rather than built as
# standalone pages.
exclude_patterns = [
    'long_description.rst',
    'description.rst',
    'install.rst',
    'tests.rst',
    'readme.rst',
    'badges.rst',
    'pypi_description.rst',
]

# Translations.
locale_dirs = ['locale/']
gettext_compact = False

pygments_style = 'sphinx'
autoclass_content = 'both'
nitpicky = True  # Warn when links are broken

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_logo = 'banniere.jpg'
htmlhelp_basename = 'PyDbLitedoc'

# -- Options for LaTeX output ------------------------------------------------

latex_documents = [
    ('index', 'PyDbLite.tex', 'PyDbLite Documentation',
     'Pierre Quentel \\& Bendik Rønning Opstad', 'manual'),
]

# -- Options for manual page output ------------------------------------------

man_pages = [
    ('index', 'pydblite', 'PyDbLite Documentation', ['Pierre Quentel'], 1),
]

# -- Options for Texinfo output ----------------------------------------------

texinfo_documents = [
    ('index', 'PyDbLite', 'PyDbLite Documentation',
     'Pierre Quentel', 'PyDbLite', 'A lightweight database engine in Python.',
     'Miscellaneous'),
]
