#!/usr/bin/env python2
import os
import requests
from lxml.html import fromstring

DIR = 'download'

def mkdir(name):
    try:
        os.makedirs(name)
    except OSError:
        pass

def main():
    r = requests.get('http://sciencehackday.pbworks.com')
    html = fromstring(r.text)

    mkdir(DIR)
    open(os.path.join(DIR, 'index.html'), 'w').write(r.text.encode('utf-8'))

    hrefs = html.xpath('id("wikipage")/descendant::a/@href')
    intralinks = filter(lambda href: href.startswith('/'), hrefs)

    for href in intralinks:
        event(href)

def event(href):
    pass
