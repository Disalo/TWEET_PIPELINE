"""Twe following script is meant for being used for the TWITTER API-V2.
The least tweepy version to use is 4.01"""

from tracemalloc import stop
import tweepy
import time
from credentials import *
import logging
import pymongo

# create a connection to the mongodb running in the mongo container of the pipeline
mongo_client = pymongo.MongoClient("mongodb")

#create a new database called twitter
db = mongo_client.twitter



##### AUTHENTICATION #####
twitter_client = tweepy.Client(bearer_token=BEARER_TOKEN,consumer_key=API_KEY,consumer_secret=API_KEY_SECRET,
access_token=ACCESS_TOKEN,access_token_secret=ACCESS_TOKEN_SECRET)


if twitter_client:
    logging.critical("\nAutentication OK")
else:
    logging.critical('\nVerify your credentials')


# Defining a query search string
query = 'climate change lang:en -is:retweet'  

search_tweets = twitter_client.search_recent_tweets(query=query,tweet_fields=['id','created_at','text'], max_results=10)
#print(search_tweets)
while True:
    for tweet in search_tweets.data:
        logging.critical(f'\n\n\nINCOMING TWEET:\n{tweet.text}\n\n\n')

        
#         # create a json record and inserting it in the collection 
        record = {'text': tweet.text, 'id': tweet.id, 'created_at': tweet.created_at}

        db.twitter.insert_one(record)

        time.sleep(10.0)
