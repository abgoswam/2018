# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:55:41 2016

@author: abgoswam
"""

import time
import threading
import redis

conn = redis.Redis()

def notrans():
    print str(conn.incr('notrans:')) + str("++")
    time.sleep(.1)
    conn.incr('notrans:', -1)

def trans():
    pipeline = conn.pipeline()
    pipeline.incr('trans:')
    time.sleep(.1)
    pipeline.incr('trans:', -1)
    print pipeline.execute()[0]
    
if 1:
    for i in xrange(3):
        threading.Thread(target=trans).start()
        
    time.sleep(.5)