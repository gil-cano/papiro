# outline for a myst_nb project with sphinx
# build with: sphinx-build -nW --keep-going -b html . ./_build/html

project = 'papiro'
copyright = '2024, Gildardo Bautista'
author = 'Gildardo Bautista García Cano'
release = '2.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'

# Add any Sphinx extension module names here, as strings.
# They can be extensions coming with Sphinx (named "sphinx.ext.*")
# or your custom ones.
extensions = [
    "myst_parser",
    # "myst_nb",
    "sphinx.ext.todo",       # 
    "sphinx_design",         # add responsive web-components to your documentation
    "sphinx_copybutton",     # add a copy button to your code blocks
    "sphinx_togglebutton",   # add collapsible content
    "sphinxcontrib.mermaid", # you will be able to add diagrams
]

# For more information see:
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = [
    "amsmath",      # for direct parsing of amsmath LaTeX environments.
    "colon_fence",  # you can also use ::: delimiters to denote code fences,\
    #  instead of ```.
    "deflist",      # you will be able to utilise definition lists
    "dollarmath",   # for parsing of dollar $ and $$ encapsulated math
    "html_image",   # you can add HTML img tags with attributes
    "linkify",      # will automatically identify “bare” web URLs and add hyperlinks
]

myst_fence_as_directive = ["mermaid"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
# html_static_path = ['_static']
# html_favicon = '_static/favicon.ico'

# Sphinx book theme customizations
# html_title = "Papiro"
# html_logo = "_static/logo.svg"


# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'
# source_suffix = {
#     '.md': 'markdown'
# }

# -- sphinx.ext.todo -----------------------
todo_include_todos = True  # Uncomment to show todos.
