import argparse
import sqlalchemy
from sqlalchemy import create_engine
from tqdm import tqdm
import faker
import random
import string
from sqlalchemy.exc import IntegrityError
db_uri = "postgresql://postgres:pass@localhost:9373"
engine = create_engine(db_uri, connect_args={'application_name': 'insert_data.py'})
connection = engine.connect()
def generate_tweet_urls(num_tweet_urls):
    for i in range(num_tweet_urls):
        tweet_id = i
        url_id = num_tweet_urls - i
        try:
            connection.execute("INSERT INTO tweet_urls (id_tweets, id_urls) VALUES (%s, %s)", (tweet_id, url_id))
            print("tweet_url", i)
        except IntegrityError as e:
            # Handle the case where the record already exists
            print(f"Skipping duplicate tweet_url: {tweet_id}, {url_id}")

generate_tweet_urls(1000000)
# Close the connection
connection.close()  
