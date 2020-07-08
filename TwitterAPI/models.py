import database as db
from sqlalchemy import create_engine,Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Tweet Class
class tweets(db.Base):
    __tablename__ = 'tweets'
    id=Column(Integer,primary_key=True,autoincrement=True)
    tweet_id = Column(String(63), nullable=False)
    fulltext = Column(Text, nullable=False)
    date = Column(DateTime)
    lang = Column(String(16))

    def __init__(self,tweet_id,fulltext,date,lang):
        self.tweet_id = tweet_id
        self.fulltext = fulltext
        self.date = date
        self.lang = lang
        