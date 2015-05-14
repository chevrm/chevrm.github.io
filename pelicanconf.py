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
I search for drugs. Bacteria, especially actinomycetes, have a reputation for biosynthesizing chemicals that are of clinical or biotechnological use.  Over half of the antibiotics approved by the FDA in the past decade are of natural origin; many more are synthetically derived from natural scaffolds.  I get my kicks from a) computationally mining genome data from these bacteria to find biosynthetic gene clusters (and predict their products)  b) understanding the regulation of these compunds (e.g. figuring out how to turn them to actually make the molecule)  and c) developing methods for engineering the gene content of these clusters to generate new and exciting compunds.
</p>
<p>
Currently, I am the Head of Experimental Genomics at Warp Drive Bio, which has built the most massive bacterial genome database in history.  I will be joining UW-Madison in 08/2015 as a member of Cameron Currie's lab to continue my research on secondary metabolites, their role in nature, and the possiblity of enrichment for novel compounds.  I will be taking an evolutionary approach to pose key questions surrounding polyketide and non-ribosomal peptide gene cluster diversity.
</p>
<p>
The model system to study this phenomenon in the <a href='http://currielab.wisc.edu/'>Currie Lab</a> is nothing short of fascinating...  Certain ants are farmers.  These ants farm (and later eat) a fungus, which is highly rich in nutrients.  Like human farmers, the ants have been faced with the challenge of pathogenic decimation of the "crop" (think the Irish Potato Famine).  To circumvent this challenge, millions of years ago, evolution selected for a symbiotic relationship in which the ants would be coated actinomycetes that could protect against bad, nasty organisms trying to steal their food.  Today, the actinobacteria that coat these ants are specific to a given colony.  Given these bacteria appear to be  a) highly prolific in secondary metabolite capability,  b) different from ant colony to colony,  and c) secondary metaoblite gene clusters tend to horizontally transfer between these and like organsisms at a relatively high rate  suggest that not only can these actinomycetes provide anti-biotic and anti-fungal protection of the ant's cultivar, they may be a prolific discovery avenue for compunds of human therapeutic and biotechnological use.
</p>
<p>
You can find me on <a href='http://twitter.com/wildtypeMC'>twitter</a> and <a href='http://www.linkedin.com/in/chevrette'>linkedIn</a>.  I have a sporadically active <a href='https://github.com/chevrm'>github</a> account. Feel free to contact me at chevrm (at) gmail (dot) com!
</p>
'''}

PROJECTS = [{'name': 'This is project 1',
                'url': 'https://github.com/a;sldfjldfja;sjf',
                'description': 'This is a desc for pro1'},
            ]
