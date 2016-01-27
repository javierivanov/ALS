#!/usr/bin/env python3
import urllib.request as urllib
import json

url_base = 'http://elk-master.osf.alma.cl:9200'
headers = {}
headers['Content-Type'] = 'application/json'
results = list()

def scroll():
    """
    Obtiene el primer resultado incluyendo el Scroll_id para continuar obteniendo los datos.
    """
    url1 = url_base + '/aos-*/_search?q=LogLevel:Critical&scroll=1m'

    data1 = {"fields" : ["TimeStamp", "text"]}
    data1 = json.dumps(data1).encode('utf-8')

    req1 = urllib.Request(url1, data1, headers)
    res1 = urllib.urlopen(req1)

    res1 = res1.read().decode('utf-8')
    res1 = json.loads(res1)
    scroll_id = res1["_scroll_id"]
    return (scroll_id, res1['hits']['hits'])


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
    aux = reescroll(scroll_id)
    i=0
    while len(aux) != 0:
        print ("Reescrolling" + str(i))
        i+=1
        results = results + aux
        aux = reescroll(scroll_id)

if __name__ == '__main__':
    main()
