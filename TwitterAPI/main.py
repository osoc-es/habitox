# Import Libraries - Twitter API, JSON, SQLAlchemy
import tweepy
import json
import database as db
from models import tweets


with open('config.json') as config_file:
    config = json.load(config_file)

# Authentication KEYS- PRIVATE
consumer_key = config["Twitter"]["consumer_key"]
consumer_secret = config["Twitter"]["consumer_secret"]
access_token = config["Twitter"]["access_token"]
access_token_secret = config["Twitter"]["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)
api.verify_credentials()


months = {'Jan': 1,
          'Feb': 2,
          'Mar': 3,
          'Apr': 4,
          'May': 5,
          'Jun': 6,
          'Jul': 7,
          'Aug': 8,
          'Sep': 9,
          'Oct': 10,
          'Nov': 11,
          'Dec': 12
          }

# Search Tweets
with open("data.json", "w") as outfile:
    for tweet in tweepy.Cursor(api.search, q="#oSoc20", tweet_mode="extended", lang="es", monitor_rate_limit=True, wait_on_rate_limit=True).items():
        tweet_json = tweet._json

        id = tweet_json["id"]
        text = tweet_json["full_text"]
        date_array = tweet_json["created_at"].split()
        day= (int)(date_array[2])
        date =date_array[5]+"-"+(str)(months[date_array[1]])+"-"+(str)(day)
        hour = date_array[3] 
        lang = tweet_json["metadata"]["iso_language_code"]
        full_date = date + " " + hour
        
        
        if (not tweet.retweeted) and ('RT @' not in tweet_json["full_text"]):
            dbTweet = tweets(id,text.encode(encoding="utf-8"),full_date,lang)
            db.session.add(dbTweet)

        #db.session.commit()
        # print(tweet._json["metadata"]["iso_language_code"])
        #print()
        json.dump(tweet._json, outfile)
        #print(json.dumps(tweet._json, indent=2))
db.session.commit()