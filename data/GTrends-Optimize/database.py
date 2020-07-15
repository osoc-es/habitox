from sqlalchemy import create_engine,Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


# Main Engine for MySQL
user = "fbp"
password = "123456"
server_ip = "localhost"
database = "osoc"

engine = create_engine('mysql://'+user+':'+password+'@'+server_ip+'/'+database)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

