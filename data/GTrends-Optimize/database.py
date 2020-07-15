from sqlalchemy import create_engine,Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


# Main Engine for MySQL
user = os.environ.get("USER_DB")
password = os.environ.get("PASS_DB")
server_ip = os.environ.get("IP_DB")
database = os.environ.get("DB_DB")

engine = create_engine('mysql://'+user+':'+password+'@'+server_ip+'/'+database)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

