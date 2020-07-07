# Import Libraries - Twitter API, JSON, SQLAlchemy
import tweepy
import json
import sqlalchemy


# Authentication KEYS- PRIVATE
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# Create API object
api = tweepy.API(auth,wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)
api.verify_credentials()




# Search Tweets
with open("data.json","w") as outfile:
    for tweet in tweepy.Cursor(api.search,q="#oSoc20",tweet_mode="extended",lang="es").items(10):
        print(tweet._json["created_at"])
        print(tweet._json["full_text"])
        #print(tweet._json["metadata"]["iso_language_code"])
        print()
        json.dump(tweet._json,outfile)
        #print(json.dumps(tweet._json, indent=2))

