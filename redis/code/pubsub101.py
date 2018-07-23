# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:25:25 2016

@author: abgoswam
"""
import time
import threading
import redis

conn = redis.Redis()

def publisher(n):
    time.sleep(1)
    for i in xrange(n):
        conn.publish('channel', i)
        time.sleep(10)
        
def run_pubsub():
    threading.Thread(target=publisher, args=(3,)).start()
    pubsub = conn.pubsub()
    pubsub.subscribe(['channel'])
    count = 0
    for item in pubsub.listen():
        print item
        count += 1
        if count == 4:
            pubsub.unsubscribe()
        if count == 5:
            break
        
if __name__ == '__main__':
    run_pubsub()