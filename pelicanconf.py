#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marc G Chevrette'
SITENAME = u'Marc G Chevrette'
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
I search for drugs.
</p>
Bacteria, especially actinomycetes, have a reputation for biosynthesizing chemicals that are of clinical or biotechnological use.  Over half of the drugs approved by the FDA in the past decade are of natural origin and many more are synthetically derived from natural scaffolds.  I get my kicks from a) computationally mining genome data from these bacteria to find biosynthetic gene clusters (and predict their chemical products), b) understanding the regulation of these compounds (e.g. figuring out how to coax them to make the molecule when they don't natively), and c) developing methods for engineering the gene content of these clusters towards generating new and exciting compounds.
</p>
<p>
Currently, I am the Head of Experimental Genomics at <a href='http://www.warpdrivebio.com'>Warp Drive Bio</a>, which has built the most massive bacterial genome database in history.  I will be joining UW-Madison in 08/2015 as a member of <a href='http://currielab.wisc.edu/'>Cameron Currie's</a> lab to continue my research on secondary metabolites, their role in nature, and the possibility of enrichment for novel compounds.  I will be taking an evolutionary approach to probe the chemical diversity of polyketide and non-ribosomal peptide gene clusters for drug discovery.
</p>
<p>
The model system to study this phenomenon in the <a href='http://currielab.wisc.edu/'>Currie Lab</a> is nothing short of fascinating...  Certain ants are farmers.  These ants farm (and later eat) a fungus, which is highly rich in nutrients.  Like human farmers, the ants have been faced with the challenge of pathogenic decimation of the "crop" (think the Irish Potato Famine).  To circumvent this challenge, millions of years ago evolution selected for a symbiotic relationship in which the ants would be coated actinomycetes that made compounds that could protect against bad, nasty organisms trying to steal their food.  Today, the actinobacteria that coat these ants are specific to a given colony.  Given these bacteria appear to be a) highly prolific in secondary metabolite capability, b) highly variable in their biosynthetic gene cluster content from ant colony to colony, and c) secondary metaoblite gene clusters tend to horizontally transfer between these and like organisms at a relatively high rate suggest that not only can these actinomycetes provide anti-biotic and anti-fungal protection of the ant's cultivar, they may be a prolific discovery avenue for compounds of human therapeutic and biotechnological use.  In a collaboration with the <a href='https://clardy.med.harvard.edu/'>Clardy Lab</a> at Harvard we hope to do just that.
</p>
<p>
You can find me on <a href='http://twitter.com/wildtypeMC'>twitter</a> and <a href='http://www.linkedin.com/in/chevrette'>linkedin</a>.  I have a sporadically active <a href='https://github.com/chevrm'>github</a> account, but typically you'll have to ask me for my code. Feel free to contact me at chevrm (at) gmail (dot) com!
</p>
'''}

PROJECTS = [{'name': 'This is project 1',
                'url': 'https://github.com/a;sldfjldfja;sjf',
                'description': 'This site is still under construction so it isnt wise to expect any of these links to work'},
            ]
