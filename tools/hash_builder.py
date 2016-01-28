#!/usr/bin/env python3


from nilsimsa import Nilsimsa, compare_digests
import threading
import pickle
import time

threads_size = 20

f = open("critical.bin", "rb")
data = pickle.load(f)
results = list()
for i in range(0, data.__len__()):
    results.append(0)
def worker(id, d, len_threads):
    local_counter = 0
    while local_counter < len(d):
        if type(data[local_counter]) == str:
            data[local_counter] = ''.join([i for i in data[local_counter] if not i.isdigit()])
            hex_data = Nilsimsa(data[local_counter]).hexdigest()
            results[local_counter] = (hex_data, data[local_counter])
        local_counter+=len_threads

threads = list()
for i in range(0, threads_size):
    t = threading.Thread(target=worker, args=(i, data, threads_size))
    threads.append(t)
    t.start()
    print("Working")



while True:
    print("Alive")
    stops = True
    for t in threads:
        if t.is_alive():
            stops = False
    if stops:
        break
    time.sleep(1)


counter = 0
for i in results:
    if type(i) == int:
        counter+=1
print (counter)
