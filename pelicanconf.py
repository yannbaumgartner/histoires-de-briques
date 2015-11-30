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

PLUGINS = ['tag_cloud', 'tipue_search']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'
LOCALE = 'fr_FR.utf8'

DATE_FORMATS = {
    'fr': '%-d %B %Y',
}

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

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
#SITELOGO = 'images/my_site_logo.png'
#FAVICON = 'images/favicon.png'

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives', 'search'))

#MENUITEMS = [('Home', '/'), ('Archives', '/archives.html'), ('Search', '/search.html')]

DISPLAY_TAGS_ON_SIDEBAR = 'True'
