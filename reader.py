# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:48:00 2018

@author: Chintan Maniyar
"""

import json, webbrowser
import csv
from datetime import datetime, timezone
from dateutil import parser

tweets_data_path = "data.txt"
tweets_data = {'id':[], 'text':[], 'place':[], 'time':[]}
tweets_file = open(tweets_data_path, "r")
url = 'twitter.com/statuses/'

def validateTweets(info=False):
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            
            if ((datetime.now(timezone.utc) - parser.parse(tweet['created_at'])).days < 1): 
                webbrowser.open_new_tab(url+str(tweet['id']))
                tweets_data['id'].append(tweet['id'])
                tweets_data['text'].append(tweet['text'])
                if(tweet['user']['location'] is None):
                    tweets_data['place'].append("00")
                tweets_data['place'].append(tweet['user']['location'])
                tweets_data['time'].append(tweet['created_at'])
    
        except:
            continue

    try:
        with open('prod.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(tweets_data.keys())
            writer.writerows(zip(*tweets_data.values()))
    except IOError as e:
        print(e)
    print(info)
    if info:
        for i in range(len(tweets_data['text'])):
            print("\nTweet no %d" %i)
            print("Time of origin: " + tweets_data['time'][i])
            print("Text : " + tweets_data['text'][i])
            print("Place: ", end="")
            if(tweets_data['place'][i]!=None):
                print(tweets_data['place'][i])
            else:
                print("Not available for this tweet")
