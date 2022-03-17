# Twitter_Data-Pipeline

## Project Aim:

    To build a Dockerized pipeline with ETL job.

    Keywords : Docker, Mongo, PostgreSQL, Slackbot

## This pipeline project involves three Docker containers and a Metabase dashboard container that, in short, does:
   Listens to tweets about a given keyword. User can set a maximum limit or stream continuously, depending on the keyword.
   Listened tweets are stored in a MongoDB.
   An ETL job that takes Tweets and collects metadata into a Postgres DB.
   A simple sentiment analysis is done via VaderSentiment to transform the tweet to sentiments and stored in the same table as tweets in Postgres DB.     
   Finally, a Slackbot template is provided to post Slack messages to a specific channel. The user can modify the sentiment binning to post tweets in
   good, ok or bad sentiment.
