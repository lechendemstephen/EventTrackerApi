# CREATING A CONNECTION TO THE POSTGRES DATABASE 
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Finalbaba1@localhost/EventTracker'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# creating a writer for the db 

def get_db(): 
    db = SessionLocal()
    try: 
        yield db
    finally: 
        db.close()