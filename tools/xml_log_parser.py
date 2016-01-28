#!/usr/bin/env python3
import urllib.request as urllib
import pickle
import os, sys
from xml.etree import ElementTree
import nilsimsa
from datetime import date, timedelta
import gzip
import threading
import time



base_directory = 'data/'


files = os.listdir(base_directory)

print (files)
