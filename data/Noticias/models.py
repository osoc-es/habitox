import database as db
from sqlalchemy import create_engine,Column, Integer, String, Text, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class trend(db.Base):
    __tablename__ = 'trends'
    id=Column(Integer,primary_key=True,autoincrement=True)
    group = Column(String(128))
    name = Column(String(128))
    date = Column(Date)
    weight = Column(Integer)
    
    def __init__(self,group,name,date,weight):
        self.group = group
        self.name = name
        self.date = date
        self.weight = weight

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

class news(db.Base):
    __tablename__ = 'news'
    id=Column(Integer,primary_key=True,autoincrement=True)
    date = Column(DateTime)
    key_words = Column(String(255))
    description = Column(Text)

    def __init__(self,date,key_words,description):
        self.date = date
        self.key_words = key_words
        self.description = description