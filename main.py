# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 13:43:42 2018

@author: Chintan Maniyar
"""

import streaming, reader, geocode, maps

LIMIT = 50 #No of tweets to fetch 

if __name__ == "__main__":
    
    #fetch tweets
    streaming.fetchTweets(LIMIT)
    
    #validate the authenticity of the tweets, info prints the tweet information on the console
    reader.validateTweets(info=True)
    
    #generate geocodes for map markers
    geocode.generateGeocodes()
    
    #pull up the map
    maps.showMap()
    
    
    