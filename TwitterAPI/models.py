import database as db
from sqlalchemy import create_engine,Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Tweet Class
class tweets(db.Base):
    __tablename__ = 'tweets'
    id = Column(String(63), primary_key=True)
    fulltext = Column(Text, nullable=False)
    date = Column(DateTime)
    lang = Column(String(16))

    def __init__(self,id,fulltext,date,lang):
        self.id = id
        self.fulltext = fulltext
        self.date = date
        self.lang = lang
        