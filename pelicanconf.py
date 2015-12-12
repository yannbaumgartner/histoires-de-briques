#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yann Baumgartner'
SITENAME = u'Histoires de briques'
SITESUBTITLE = 'Un site dédié aux LEGO®'
SITEURL = ''
GITHUB_URL = 'https://github.com/yannbaumgartner/histoires-de-briques.git'

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images']
PLUGIN_PATHS = ['plugins']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.png'}
}

PLUGINS = ['tag_cloud', 'tipue_search']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'
LOCALE = 'fr_FR.utf8'

DATE_FORMATS = {
    'fr': '%-d %B %Y',
}

DEFAULT_PAGINATION = False

SUMMARY_MAX_LENGTH = none

THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives', 'search'))

DISPLAY_TAGS_ON_SIDEBAR = 'True'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)
