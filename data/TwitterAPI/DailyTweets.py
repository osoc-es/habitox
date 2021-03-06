# Import Libraries - Twitter API, JSON, SQLAlchemy - Requirements.txt
import tweepy
import json
import database as db
from models import tweets
from datetime import datetime
import os

# Authentication KEYS - PRIVATE
consumer_key = os.environ.get("consumer_key-Twitter")
consumer_secret = os.environ.get("consumer_secret-Twitter")
access_token = os.environ.get("access_token-Twitter")
access_token_secret = os.environ.get("access_token_secret-Twitter")


# Give the Auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)
api.verify_credentials()

# Map to translate Months to numbers
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
        

# Search KeyWords
keyWords = ["futbol", "deporte en casa", "ejercicio", "fitness", "bicicleta", "cardio", "just dance", "Bárbara de Regil", "adelgazar", "GAP", "postre", "tarta", "pan", "reposteria", "bolleria", "recetas", "cocina en casa", "dieta", "cocina saludable", "cerveza", "diy", "educacion", "manualidades", "coco melon", "dibujos animados", "peppa pig", "la patrulla canina", "tutorial",
         "the office", "zoom", "teams", "discord", "google meet", "slack", "jitsi", "ordenador", "portatil", "monitor", "webcam", "microfono", "respondus", "ERTE", "proctoring", "moodle", "moodle exams", "fase 1", "restricciones", "aeropuerto", "mascarilla", "guantes", "normativa", "sintomas", "wuhan", "hospitales", "centros de salud", "remedios", "aplausos", "resistire", "caceroladas","#conmigo"]

# Iterate every KeyWord
for i in keyWords:
    print(i)
    j=0 # Counter for number of tweets
    for tweet in tweepy.Cursor(api.search, q=i+" -filter:retweets", tweet_mode="extended", lang="es", monitor_rate_limit=True, wait_on_rate_limit=True,since=datetime.today().strftime('%Y-%m-%d')).items():
        
        tweet_json = tweet._json
        # Get Data we need and manipulate it
        id = tweet_json["id"]
        text = tweet_json["full_text"]
        date_array = tweet_json["created_at"].split()
        day = (int)(date_array[2])
        date = date_array[5]+"-"+(str)(months[date_array[1]])+"-"+(str)(day)
        hour = date_array[3]
        lang = tweet_json["metadata"]["iso_language_code"]
        full_date = date + " " + hour

        if (not tweet.retweeted) and ('RT @' not in tweet_json["full_text"]): # Remove the retweets
            print(date+" : "+text)
            j+=1
            # Create object and add to database 
            dbTweet = tweets(id, text.encode(encoding="utf-8"), full_date, lang)
            db.session.add(dbTweet)
            # Commit to 100 batches
            if(j%100==0):
                print("Batch of 100")
                db.session.commit()
    # Secure Commit- Not all are going to be commited in 100
    db.session.commit()
# Last commit
db.session.commit()
    
