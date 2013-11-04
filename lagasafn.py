#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Downloads and updates the lagasafn

import requests
import BeautifulSoup

index_url = 'http://www.althingi.is/altext/stjtnr.html'

html = requests.get(index_url).content
soup = BeautifulSoup.BeautifulSoup(html)

list_of_laws = soup.findAll('a')
len_laws = len(list_of_laws)

for i, law in enumerate(list_of_laws):
    # Skip all links that to not link to a specitic law
    href = law['href']
    if '/altext/stjt/' not in href:
        continue
    law_name = law.text
    # Convert id of the law so year comes first
    sequence, year = law_name.split('/')
    percent_done = float(i) / len_laws * 100
    new_law_name = "%s-%s" % (year, sequence)
    print "%i%% done. Downloading %s..." % (percent_done, law_name),
    html = requests.get('http://www.althingi.is%s' % href).content
    filename = './%s' % href
    with open(filename,'w') as f:
        f.write(html)
    print "ok"
    
