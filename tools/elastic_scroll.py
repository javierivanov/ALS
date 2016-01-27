#!/usr/bin/env python3
import urllib.request as urllib
import json


headers = {}
headers['Content-Type'] = 'application/json'


url1 = 'http://elk-master.osf.alma.cl:9200/aos-*/_search?q=LogLevel:Critical&scroll=1m'

data1 = '{"fields" : ["TimeStamp", "text"]}'
data1 = data1.encode('utf-8')

req1 = urllib.Request(url1, data1, headers)
res1 = urllib.urlopen(req1)

res1 = res1.read().decode('utf-8')
res1 = json.loads(res1)


scroll_id = res1["_scroll_id"]

def reescroll():
    url2 = 'http://elk-master.osf.alma.cl:9200/_search/scroll'
    data2 = {"scroll": "1m", "scroll_id": scroll_id}
    data2 = json.dumps(data2).encode('utf-8')

    req2 = urllib.Request(url2, data2, headers)
    res2 = urllib.urlopen(req2)

    res2 = res2.read().decode('utf-8')
    res2 = json.loads(res2)
