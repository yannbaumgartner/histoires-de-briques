#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yann Baumgartner'
SITENAME = u'Histoires de briques'
SITESUBTITLE = 'Un site dédié aux LEGO®'
SITEURL = 'https://github.com/yannbaumgartner/histoires-de-briques'
GITHUB_URL = 'https://github.com/yannbaumgartner/histoires-de-briques.git'
TIMEZONE = 'Europe/Zurich'
DEFAULT_LANG = u'fr'
LOCALE = 'fr_FR.utf8'
DATE_FORMATS = {
    'fr': '%-d %B %Y',
}

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.png']
PLUGIN_PATHS = ['plugins']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.png': {'path': 'favicon.png'}
}

PLUGINS = ['tag_cloud', 'tipue_search']

DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = None

THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives', 'search'))
SEARCH_URL = '/search.html'

DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_TAGS_ON_SIDEBAR = 'True'
SHOW_ARTICLE_AUTHOR = 'True'

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
