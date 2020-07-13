from sqlalchemy import create_engine,Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



# Main Engine for MySQL
engine = create_engine('mysql://fbp:123456@localhost/osoc')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

