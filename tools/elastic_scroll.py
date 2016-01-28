#!/usr/bin/env python3
import urllib.request as urllib
import json
import pickle
import os, sys

import nilsimsa


url_base = 'http://elk-master.osf.alma.cl:9200'
headers = {}
headers['Content-Type'] = 'application/json'
results = list()
size_pack = 100000
def scroll():
    """
    Obtiene el primer resultado incluyendo el Scroll_id para continuar obteniendo los datos.
    """
    url1 = url_base + '/aos-*/_search?q=LogLevel:Error&scroll=1m'

    data1 = {"fields" : ["TimeStamp", "text"], "size": size_pack}
    data1 = json.dumps(data1).encode('utf-8')

    req1 = urllib.Request(url1, data1, headers)
    res1 = urllib.urlopen(req1)

    res1 = res1.read().decode('utf-8')
    res1 = json.loads(res1)
    scroll_id = res1["_scroll_id"]
    return (scroll_id, res1['hits'])


def reescroll(scroll_id):
    """
    Reutiliza el scroll_id para continuar obteniendo los datos.
    """
    url2 = url_base + '/_search/scroll'
    data2 = {"scroll": "1m", "scroll_id": scroll_id}
    data2 = json.dumps(data2).encode('utf-8')

    req2 = urllib.Request(url2, data2, headers)
    res2 = urllib.urlopen(req2)

    res2 = res2.read().decode('utf-8')
    res2 = json.loads(res2)

    return res2['hits']['hits']


def main():
    scroll_id, results = scroll()
    size = int(results['total'])
    results = results['hits']
    aux = reescroll(scroll_id)
    size-=size_pack
    while len(aux) != 0:
        size-=size_pack
        print ("Reescrolling\tdata left: " + str(size))
        results = results + aux
        aux = reescroll(scroll_id)
    f = open("data.pickled", "wb")

    print("Saving data...")
    pickle.dump(results, f)
    f.flush()
    f.close()
    print("End EXECUTION")

if __name__ == '__main__':
    main()
