#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'James Loach'
SITENAME = 'James Loach'
SITEURL = 'http://jamesloach.com'
THEME = 'theme/'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'



# From old config file
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
STATIC_PATHS = ['images', 'papers', 'extra/favicon.ico']
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
ARTICLE_EXCLUDES = ['in_progress']
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['render_math', 'ipynb.markup', 'tipue_search', 'sitemap'] 

# Additions for ipynb
IGNORE_FILES = ['.ipynb_checkpoints', 'standalone.md', 'python.ipynb']
MARKUP = ('md', 'ipynb')
IPYNB_SKIP_CSS = True
IPYNB_USE_METACELL = True

# Additions for tipuesearch
DIRECT_TEMPLATES = ['index', 'search']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
