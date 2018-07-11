# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:48:00 2018

@author: Chintan Maniyar
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

class StdOutListener(StreamListener):
    fh = open('t.txt', 'w')
    limit = 0
    count = 0

    def __init__(self, limit):
        self.limit = limit
    
    def on_data(self, data):
        self.count += 1
        print(self.count)
        print(data)
        self.fh = open('data.txt', 'a')
        self.fh.write(data)
        self.fh.close()
        if self.count < self.limit:
            return True
        else:
            print("exiting")
            return False
    
    def on_error(self, status):
        print(status)
    
def fetchTweets(limit):
    StdOutListener.fh = open('data.txt', 'a')
    l = StdOutListener(limit)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track = ['BlueGreenAlgae', 'CyanoBacteria', 'cyanotracker', 'anabaena', 'microcystis', 'cyanotoxins', 'toxic algae', 'algae bloom', 'algal bloom', '#CyanoBacteria', '#AlgaeBloom', '#CitSci', '#CyanoBacteriaBlooms']) 
