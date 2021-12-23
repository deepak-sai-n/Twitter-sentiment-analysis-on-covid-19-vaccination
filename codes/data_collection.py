# Required libraries

import tweepy
import pandas as pd
import json
import re
import os
import time
from datetime import datetime, date, timedelta


# Data collection using twitter api

# Authenticate to Twitter

access_token="1450533290822103040-kQbtEHprUX0tAUTEB8jUboLFJBMwXn"
access_token_secret="InRSqCrHRfoqPZA6ni4z1iqGBixO8NbPMMGO8jbeH9ICh"
consumer_key="T39BTH4dIS5MMNqsO6LLESDmf"
consumer_secret="nNmvqBjrLw8exwpftNd11tGxLZjY73VCxKEer3HhZJG7sUebig"


#API access
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


#api connection request to tweepy
class MyStreamListener(tweepy.Stream):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")


# Generate list of dates (7 days window) based on today's date
list_of_dates = []
today = date.today()
for i in range(-7,1):
    target_date = (today + timedelta(days=i)).strftime("%Y-%m-%d")
    list_of_dates.append(target_date)

# search terms used to get the tweets which are related to the topic and specifying the number of tweets extracted
list_of_dicts = []
search_term = 'covid covid-19 vaccination'
num_tweets = 100000


#Function to Extract specific details like username,location,text from each tweet
def get_tweets(search_term = search_term, num_tweets = num_tweets):
    
    for end_date in list_of_dates:
        start_date = (datetime.strptime(end_date, '%Y-%m-%d') - timedelta(days=1)).strftime("%Y-%m-%d") # Create 1-day windows for extraction
        tweet_count = len(list_of_dicts)

        for tweet in tweepy.Cursor(api.search_tweets,  #searh for tweets in the specific time range 
                                   q=f'{search_term} since:{start_date} until:{end_date}',
                                   lang = 'en',
                                   count = num_tweets,
                                   tweet_mode = 'extended').items(num_tweets):
            if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
                if tweet.lang == "en":  #only tweets in english are considered 
                    tweet_dict = {} #dictonary of various Key-Value pairs
                    tweet_dict['username'] = tweet.user.name
                    tweet_dict['location'] = tweet.user.location
                    tweet_dict['text'] = tweet.full_text
                    #tweet_dict['fav_count'] = tweet.favorite_count  
                    tweet_dict['hashtags'] = tweet.entities['hashtags']
                    tweet_dict['tweet_date'] = tweet.created_at
                    list_of_dicts.append(tweet_dict)  
                    tweet_count +=1
                    if tweet_count%100 ==0:
                        print(f'Extracted tweet count = {tweet_count}')
                
        #print(f'Completed extraction for {start_date} to {end_date}. Sleep for 15 mins')

#Data Consolidation
#Export the obtained data frame of tweet and its details into a csv file
get_tweets()
tweets_df = pd.DataFrame(list_of_dicts)
tweets_df.to_csv('data\\collected_tweets3.csv',index=False)