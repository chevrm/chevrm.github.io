#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marc Chevrette'
SITENAME = u'MG Chevrette'
SITESUBTITLE = u'Mining Secondary Metabolism'
SITEURL = 'http://chevrm.github.io'

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

# Theme declaration
THEME = './elegant'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Currie Lab', 'http://currielab.wisc.edu/'),
         ('Wisconsin Genetics', 'http://www.genetics.wisc.edu/'),
         ('Warp Drive', 'http://www.warpdrivebio.com'),)

# Social widget
SOCIAL = (('twitter', 'http://www.twitter.com/wildtypeMC'),
          ('linkedin', 'http://www.linkedin.com/in/chevrette'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

LANDING_PAGE_ABOUT = {'title': 'Mining Secondary Metabolism', 'details':
'''
<p>
This is a placeholder.
</p>
<p>
This is also a placeholder.
</p>
<p>
You guessed it.  This, too.
</p>
<p>
You can find me on <a href='http://twitter.com/wildtypeMC'>twitter</a> and <a href='http://www.linkedin.com/in/chevrette'>linkedIn</a>.  I have a sporadically active <a href='https://github.com/chevrm'>github</a> account. Feel free to contact me at chevrm (at) gmail (dot) com!
</p>
'''}

PROJECTS = [{'name': 'This is project 1',
                'url': 'https://github.com/a;sldfjldfja;sjf',
                'description': 'This is a desc for pro1'},
            ]
