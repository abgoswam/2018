# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 17:12:13 2016

@author: agoswami
"""

import unittest

#class OutcomesTest(unittest.TestCase):
#
#    def testPass(self):
#        print "111"
#        return
#
#    def testFail(self):
#        print "222"
##        self.failIf(True)
#
#    def testError(self):
#        print "333"
##        raise RuntimeError('Test error!')

class TestCh01(unittest.TestCase):
    def setUp(self):
        print "1111"
        import redis
        self.conn = redis.Redis(db=15)

    def tearDown(self):
        print "222"
#        del self.conn
        print
        print

    def test_article_functionality(self):
        print "abhishek"
        conn = self.conn
#        import pprint
#
#        article_id = str(post_article(conn, 'username', 'A title', 'http://www.google.com'))
#        print "We posted a new article with id:", article_id
#        print
#        self.assertTrue(article_id)
#
#        print "Its HASH looks like:"
#        r = conn.hgetall('article:' + article_id)
#        print r
#        print
#        self.assertTrue(r)
#
#        article_vote(conn, 'other_user', 'article:' + article_id)
#        print "We voted for the article, it now has votes:",
#        v = int(conn.hget('article:' + article_id, 'votes'))
#        print v
#        print
#        self.assertTrue(v > 1)
#
#        print "The currently highest-scoring articles are:"
#        articles = get_articles(conn, 1)
#        pprint.pprint(articles)
#        print
#
#        self.assertTrue(len(articles) >= 1)
#
#        add_remove_groups(conn, article_id, ['new-group'])
#        print "We added the article to a new group, other articles include:"
#        articles = get_group_articles(conn, 'new-group', 1)
#        pprint.pprint(articles)
#        print
#        self.assertTrue(len(articles) >= 1)
#
#        to_del = (
#            conn.keys('time:*') + conn.keys('voted:*') + conn.keys('score:*') + 
#            conn.keys('article:*') + conn.keys('group:*')
#        )
#        if to_del:
#            conn.delete(*to_del)

if __name__ == '__main__':
    unittest.main()
