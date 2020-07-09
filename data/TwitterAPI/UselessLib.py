# Libraries and cool stuff
import GetOldTweets3 as got
import database as db
from models import tweets
from datetime import date, timedelta
import time

# Main Searches --> Keypoints of projects?¿
searchWords=["teletrabajo","workingfromhome","cuarentena","CuandoEstoSeAcabe"]
# We define date to start searching from (Beginings of APOCALYPSE!)
d=date(2020,2,1)
dNext=d+timedelta(days=1) # We get the next day(In order to reduce de amount of tweets in the Data Structure of the Librarie- Really bad choice of Data Structure....)
for day in range(0,120): # 4 months roughly 120 days
    print(d)
    for i in searchWords:
        # Debug console
        print(i+"\n"+"========================================================================")
        # We get the Tweets in spanish the most popular ones, if too many only 1000
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(i).setSince(str(d)).setUntil(str(dNext)).setLang('es').setTopTweets(True).setMaxTweets(1000)
        k=0
        #print(got.manager.TweetManager.getTweets(tweetCriteria))
        try:
            # We add tweets one by one to Database
            for j in got.manager.TweetManager.getTweets(tweetCriteria):
                id=j.id
                text=j.text
                lang="es"
                date=j.date

                dbTweet = tweets(tweet_id=id, fulltext=text.encode(encoding="utf-8"), date=date, lang=lang)
                db.session.add(dbTweet)
                k+=1
                print(i+" : "+str(k))
                if(k%100==0):
                    # In Batches of 100 
                    db.session.commit()
        except:
            # Oh boi and error(Too many requests...) - Lets wait 
            print("WAITING!")
            time.sleep(300)
            continue
        # Commit just in case
        db.session.commit()
    # next Day
    d=dNext
    dNext=d+timedelta(days=1)
    # Commit just in case
    db.session.commit()

