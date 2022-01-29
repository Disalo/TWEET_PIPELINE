
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pymongo
from sqlalchemy import create_engine

time.sleep(30)

s  = SentimentIntensityAnalyzer()

# Establish a connection to the MongoDB server
client = pymongo.MongoClient(host="mongodb", port=27017)

# Select the database to use within the MongoDB server
db = client.twitter

docs = db.twitter.find()

# Establish a connection to the Postgres server
pg = create_engine('postgresql://postgres:loop@postgresdb:5432/postgres', echo=True)

# Query to create table
pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text TEXT,
    sentiment NUMERIC,
    id SERIAL
);
''')
# Loop to insert every tweet from MongoDB to Postgresql
while True:
    for doc in docs:
        sentiment = s.polarity_scores(doc['text'])
        print(sentiment)
        text = doc['text']
        score = sentiment['compound']
        query = "INSERT INTO tweets VALUES (%s, %s);"
        pg.execute(query, (text, score))
        time.sleep(10)
