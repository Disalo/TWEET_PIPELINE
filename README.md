# Twitter_Data-Pipeline

## Project Aim:
To orchestrate a data pipeline with five containers: 1.tweet_collector, 2.mongodb, 3.etl_job, 4.postgresdb, 5.slack_bot <br />
To build a Dockerized pipeline with ETL job.

## The ETL pipeline involves five Docker containers:
   - tweet_collector container: Listens to tweets about a given keyword(here is 'climate change', but it could be changed within 'get_tweets.py').
   - mongodb container: Listened tweets are stored in a MongoDB.
   - etl_job container: An ETL job that takes Tweets and collects metadata into a Postgres DB.
   A simple sentiment analysis is done via VaderSentiment to transform the tweet to sentiments and stored in the same table as tweets in Postgres DB.
   - postgresdb container: To store tweets on postgres database after transfomation along with sentiment analysis.
   - slack_bot container: Finally, a Slackbot template is provided to post Slack messages to a specific channel. The data is read from postgres database, based on last tweet stored on.

## Run
Simply open a terminal on the folder(where docker-compose.yml file is), and give 'docker-compose up' command. It will automatically pull and download images and create required images as defined in .yml fils. <br />
Each container could be accessed through 'cli' in docker app. <br />
For interacteion with mongo 'docker exec -it container_id mongo' could be given. <br />
For interacteion with postgres 'docker exec -it container_id psql -p 5432 -U postgres' could be given.
