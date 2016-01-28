#!/usr/bin/env python3
import urllib.request as urllib
import pickle
import os, sys
from xml.etree import ElementTree as et
import nilsimsa
from datetime import date, timedelta
import gzip
import threading
import time



base_directory = 'data2/'


files_ = os.listdir(base_directory)
files = list()
for i in files_:
    if i.endswith(".bin"):
        files.append(i)

bigList = list()

for i in files:
    print(i)
    temp_file = open(base_directory + i, 'rb')
    temp_data = pickle.load(temp_file)
    bigList = bigList + temp_data

root = et.fromstring(bigList[100])
print (root.tag)
print (root.text)
