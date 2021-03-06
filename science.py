#!/usr/bin/env python
import os
import requests
from lxml.html import fromstring, tostring

DIR = 'download'
BASEURL = 'http://sciencehackday.pbworks.com'

def mkdir(name):
    try:
        os.makedirs(name)
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
            download_event(href)
        print_event_text(href)

def download_event(href):
    r = requests.get(BASEURL + href)

    print href
    print r.status_code

    mkdir(DIR + os.path.split(href)[0])
    open(DIR + href, 'w').write(r.text.encode('utf-8'))

def print_event_text(href):
    html = fromstring(open(DIR + href).read())
    anchors = html.xpath('id("wikipage")/descendant::a')
    for a in anchors:
        # print mediawiki syntax
        hrefs = a.xpath('@href')
        text = a.text_content()
        if len(hrefs) == 0:
            print ' * %s' % text.encode('utf-8')
        else:
            print '* [%s %s]' %  (hrefs[0].encode('utf-8'), text.encode('utf-8'))

if __name__ == '__main__':
    main()
