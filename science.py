#!/usr/bin/env python2
import os
import requests
from lxml.html import fromstring

DIR = 'download'
BASEURL = 'http://sciencehackday.pbworks.com'

def mkdir(name):
    try:
        os.makedirs(name)
        print 'mkdir', name
    except OSError:
        pass

def main():
    r = requests.get(BASEURL)
    html = fromstring(r.text)

    mkdir(DIR)
    open(os.path.join(DIR, 'index.html'), 'w').write(r.text.encode('utf-8'))

    hrefs = html.xpath('id("wikipage")/descendant::a/@href')
    intralinks = filter(lambda href: href.startswith('/'), hrefs)

    for href in intralinks:
        if not os.path.exists(DIR + href):
            event(href)

def event(href):
    r = requests.get(BASEURL + href)
    html = fromstring(r.text)

    print href
    print r.status_code

    mkdir(DIR + os.path.split(href)[0])
    open(DIR + href, 'w').write(r.text.encode('utf-8'))

if __name__ == '__main__':
    main()
