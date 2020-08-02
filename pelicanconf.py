#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from datetime import datetime

AUTHOR = 'Govind KP'
SITENAME = 'Digressions - A blog'
SITETITLE = 'Digressions - A blog'
SITESUBTITLE = 'Govind KP'
SITEURL = ''
RELATIVE_URLS = True

BROWSER_COLOR='#333333'
PYGMENTS_STYLE='monokai'
THEME_COLOR = 'light'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = False
THEME_COLOR_ENABLE_USER_OVERRIDE = False

PATH = 'content'
OUTPUT_PATH = 'public'
STATIC_PATHS = [
    # 'images',
    'extra',  # this
]

SITEMAP = {'format': 'xml'}
PLUGIN_PATHS = [
    'plugins/sitemap/pelican/plugins',
    'plugins/render_math/pelican/plugins',
    'plugins/simple_footnotes/pelican/plugins',
    'plugins',
]
PLUGINS = [
    'sitemap',
    'render_math',
    'simple_footnotes',
    'neighbors',
    'post_stats',
]

# CC_LICENSE = {
#     'name': 'Creative Commons Attribution-ShareAlike',
#     'version': '4.0',
#     'slug': 'by-sa'
# }
COPYRIGHT_YEAR = datetime.now().year


EXTRA_PATH_METADATA = {
    # 'extra/custom.css': {'path': 'custom.css'},
    'extra/robots.txt': {
        'path': 'robots.txt'
    },
    'extra/logo.jpg': {
        'path': 'logo.jpg'
    },
    'extra/favicon.ico': {
        'path': 'favicon.ico'
    },
    'extra/CNAME': {
        'path': 'CNAME'
    },
    'extra/LICENSE': {
        'path': 'LICENSE'
    },
    'extra/README': {
        'path': 'README'
    },
}

THEME = './theme/Flex'
SITELOGO = SITEURL + '/logo.jpg'
USER_LOGO_URL = SITEURL + '/logo.jpg'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
# SOCIAL = (('Github', 'https://github.com/reisub0/'), )
SOCIAL = (
    ('github', 'https://github.com/reisub0/'),
    ('gitlab', 'https://gitlab.com/reisub0/'),
    ('linkedin', 'https://linkedin.com/in/govind-kp/'),
    ('rss', '/feeds/all.atom.xml'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
