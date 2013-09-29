We copy resources from disparate
[Science Hack Day wiki pages](http://sciencehackday.pbworks.com)
into one [book about citizen science](https://en.wikibooks.org/wiki/Citizen_Science).

Run this to return links in mediawiki syntax.

    ./science.py

Separate Twitter.

    ./science.py | grep twitter | sed 's+http://+https://+' | sort -u
    ./science.py | grep -v twitter
