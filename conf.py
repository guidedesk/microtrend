# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add paths if your modules are outside the project root
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Trend Micro Installation & Activation Guide'
copyright = '2025, Trend Micro'
author = 'Trend Micro Support Team'

# Full version string
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

# Allow raw HTML inside .rst files
raw_enabled = True

templates_path = ['_templates']

# Ignore these files/folders during build
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Allow unsafe HTML content
html_allow_unsafe = True

# -- Options for HTML output -------------------------------------------------

# HTML theme (you can enable sphinx_rtd_theme if installed)
# html_theme = 'sphinx_rtd_theme'

html_title = "Trend Micro Installation & Activation Guide"
html_short_title = "Trend Micro Setup"
html_favicon = 'favicon.ico'  # Put favicon in _static or root folder

# Hide "View Source" link
html_show_sourcelink = False

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Directory for custom static files like CSS, JS, images
# html_static_path = ['_static']
g
