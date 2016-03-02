#!/usr/bin/env python

import scraperwiki
import requests
import json
from collections import Counter

url = 'https://premium.scraperwiki.com/x0hdcrq/mw20fbg1d0nharn/sql/?q=select%20%0A%09caption%0Afrom%20swdata%0A--%20where%20userurl%20%3E%20%0Aorder%20by%20description%0A'
media = json.loads(requests.get(url).text)
print media
fulllist = []
for caption in media:
    wordlist = caption['caption'].split(' ')
    for word in wordlist:
        fulllist.append(word)
        print fulllist
counts = Counter(fulllist)
print counts


# Saving data:
# unique_keys = [ 'id' ]
# data = { 'id':12, 'name':'violet', 'age':7 }
# scraperwiki.sql.save(unique_keys, data)
