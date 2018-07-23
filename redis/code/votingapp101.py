# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 08:10:36 2016

@author: abgoswam
"""
import redis
import time

ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432
def article_vote(conn, user, article):
	cutoff = time.time() - ONE_WEEK_IN_SECONDS
	if conn.zscore('time:', article) < cutoff:
		return
	article_id = article.partition(':')[-1]
	if conn.sadd('voted:' + article_id, user):
		conn.zincrby('score:', article, VOTE_SCORE)
		conn.hincrby(article, 'votes', 1)

def display(conn, article_id):
    print "Display 'article:<article_id>' (which is a hash)"
    print conn.hgetall('article:' + article_id)
    print
    
    print "Display 'voted:<article_id>'  (which is a set of users who have voted on that article)"
    print conn.smembers('voted:' + article_id)
    print 
    
    print "Display 'score:' which is a sorted set of articles by score"
    print conn.zrange('score:', 0, -1, withscores=True)
    print

    print "Display 'time:' which is a sorted set of articles by posted time"
    print conn.zrange('time:', 0, -1, withscores=True)
    print  
  
if __name__ == '__main__':
    conn = redis.Redis(db=15)
    
#    We want to add a new article to the pool of articles.
    user= "AG"
    title="black friday deals"
    link="http://blackfriday.com"
    article_id = str(conn.incr('article:'))     #A
        
    voted = 'voted:' + article_id
    conn.sadd(voted, user)                      #B
    conn.expire(voted, ONE_WEEK_IN_SECONDS)     #B

    now = time.time()
    article = 'article:' + article_id
    conn.hmset(article, {                       #C
        'title': title,                         #C
        'link': link,                           #C
        'poster': user,                         #C
        'time': now,                            #C
        'votes': 1,                             #C
    })                                          #C

    conn.zadd('score:', article, now + VOTE_SCORE)  #D
    conn.zadd('time:', article, now)                #D

    print "We posted a new article with id:", article_id
    print 

    display(conn, article_id)
    
    print "Another user (DG) votes on that article"
    user2="DG"
    
    if conn.sadd('voted:' + article_id, user2):      #E
        conn.zincrby('score:', article, VOTE_SCORE) #E
        conn.hincrby(article, 'votes', 1)           #E
    
    display(conn, article_id)
    
    