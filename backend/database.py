from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

import socket
from dotenv import load_dotenv

load_dotenv()

def get_database_url():
    url = os.getenv("DATABASE_URL")
    if url:
        return url
    
    # Try to resolve 'db' host to see if we are in docker-compose
    try:
        socket.gethostbyname("db")
        return "postgresql://user:password@db:5432/oilquest"
    except socket.error:
        return "postgresql://user:password@localhost:5432/oilquest"

DATABASE_URL = get_database_url()
print(f"Using Database URL: {DATABASE_URL}")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Import models here to ensure they are registered with Base
from models import *

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
