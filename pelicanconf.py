#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marc G Chevrette'
SITENAME = u'Marc Chevrette'
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
I dig around for drugs.
</p>
Bacteria, especially actinomycetes, have a reputation for biosynthesizing chemicals that are of clinical or biotechnological use.  Over half of the drugs approved by the FDA in the past decade are of natural origin and many more are synthetically derived from natural scaffolds.  I get my kicks from a) computationally mining genome data from these bacteria to find novel biosynthetic gene clusters (and predict their chemical products), b) understanding the regulation of these compounds (e.g. figuring out how to coax them to produce molecule when conditions for expression in nature are unknown), and c) developing methods of engineering the gene content of these clusters towards generating even more chemical diversity.
</p>
<p>
Until recently, I was the Head of Experimental Genomics at <a href='http://www.warpdrivebio.com'>Warp Drive Bio</a>, which has built the most massive bacterial genome database in history to exploit gene cluster diversity for the discovery of novel therapeutics and exciting biosynthesis.  I joined <a href='http://www.genetics.wisc.edu/'>UW-Madison Genetics</a> in 08/2015 as a member of <a href='http://currielab.wisc.edu/'>Cameron Currie's lab</a> to continue my research on secondary metabolites, their role in nature, and the possibility of enrichment for novel compounds of therapeutic use.  I will be taking an evolutionary approach to probe the chemical diversity of polyketide and non-ribosomal peptide gene clusters in our model system for drug discovery.
</p>
<p>
The model system to study this phenomenon in the <a href='http://currielab.wisc.edu/'>Currie Lab</a> is nothing short of fascinating.  Certain ants are farmers.  These ants farm (and later eat) a fungus, which is highly rich in nutrients.  Like human farmers, the ants have been faced with the challenge of pathogenic decimation of their "crop" (think the Irish Potato Famine).  To circumvent this challenge, millions of years evolution has selected for a symbiotic relationship in which the ants have become coated with actinomycetes that can synthesize chemical compounds to protect against bad, nasty organisms trying to steal their food.  Today, the actinobacterial strains that coat these ants are specific to a given colony.
</p>
<center>
<figure>
<img src="images/antsfig2.png" alt="Leaf-Cutter System">
<figcaption><font size="4">Photo: Klassen, J. L. (2014). Microbial secondary metabolites and their impacts on insect symbioses. Current Opinion in Insect Science, 4, 15–22. http://doi.org/10.1016/j.cois.2014.08.004</font></figcaption>
</figure>
</center>
<p>
These bacteria appear to a) be highly prolific in secondary metabolite capability, b) be highly variable in their biosynthetic gene cluster content from ant colony to colony, and c) have genomes that show much evidence of horizontal transfer of secondary metaoblite gene clusters.  Our hypothesis is that not only can these actinomycetes provide anti-biotic and anti-fungal protection of the ant's cultivar, they may be a prolific discovery avenue for compounds of human therapeutic and biotechnological use.
</p>
<p>
The likelihood of a gene cluster under high selective pressure to hit a eukaryotically conserved target (and thus a medically relevant target) is relatively high when you consider that millions of years of selective evolution are on our side.
</p>
<p>
Nature is spending a lot of energy to make these molecules, so it follows that they must be making them for a biological reason.  In a variety of collaborations we hope to prove exactly that while uncovering the evolutionary mechanisms of biosynthesis.
</p>
<p>
You can find me reliably on <a href='http://twitter.com/wildtypeMC'>twitter</a> and <a href='http://www.linkedin.com/in/chevrette'>linkedin</a>.  I have a sporadically active <a href='https://github.com/chevrm'>github</a> account, but typically you will have to ask me for my code. Do not be shy!  Feel free to contact me at chevrm (at) gmail (dot) com!
</p>
'''}

PROJECTS = [	{'name': 'Twitter',
		'url': 'http://twitter.com/wildtypeMC',
		'description': ''},
		{'name': 'LinkedIn',
		'url': 'http://www.linkedin.com/in/chevrette',
		'description': ''},
		{'name': 'CV',
                'url': 'https://github.com/chevrm/cv/raw/master/ChevretteCV.pdf',
                'description': 'PDF download of my CV.'},
		{'name': 'Google Scholar',
		'url': 'https://scholar.google.com/citations?user=VX3Laf8AAAAJ&hl=en',
		'description': 'Links to my publications.'},
		{'name': 'Video: Leaf-Cutter Ants',
		'url': 'https://www.youtube.com/watch?v=Xxnmh4IDYaU',
		'description': 'A brief video from the NSF outlining major areas of research in the Currie Lab.'},
		{'name': 'Currie Lab Homepage',
		'url': 'http://currielab.wisc.edu/',
		'description': ''},
		{'name': 'Warp Drive Bio',
		'url': 'http://www.warpdrivebio.com/',
		'description': ''},
]
