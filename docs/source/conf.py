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

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


# -- Project information -----------------------------------------------------

project = 'intrst_algrms'
copyright = '2019, Niccolum'
author = 'Niccolum'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.linkcode'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# additional custom configs
master_doc = 'index'
autodoc_mock_imports = ["iteration_utilities", "more_itertools"]


def linkcode_resolve(domain, info):

    def get_line(filename, component_name):
        # hardcode for search first line in implementation, not name in comments
        import re
        import urllib
        raw_link = "https://raw.githubusercontent.com/Niccolum/intrst_algrms/master/%s.py" % filename
        req = urllib.request.urlopen(raw_link)
        patterns = (re.compile(b'%s.*(\\|:)?$' % attr.encode()) for attr in component_name.split('.'))
        pat = next(patterns)
        for num, line in enumerate(req, start=1):
            if pat.search(line):
                try:
                    pat = next(patterns)
                except StopIteration:
                    return num

    if domain != 'py':
        return None
    if not info['module']:
        return None
    filename = info['module'].replace('.', '/')
    line = get_line(filename, info['fullname'])
    link = "https://github.com/Niccolum/intrst_algrms/tree/master/{}.py#L{}".format(filename, line)
    return link
