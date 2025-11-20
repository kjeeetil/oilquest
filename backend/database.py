from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

import socket
from dotenv import load_dotenv

load_dotenv()

def get_database_url():
    # 1. Prefer explicit env var
    url = os.getenv("DATABASE_URL")
    if url:
        print(f"Found DATABASE_URL env var: {url}")
        return url
    
    # 2. Try to resolve 'db' host (Docker Compose)
    try:
        socket.gethostbyname("db")
        print("'db' host resolved. Using docker connection.")
        return "postgresql://user:password@db:5432/oilquest"
    except socket.error:
        pass

    # 3. Fallback to SQLite
    print("Could not resolve 'db' host and no DATABASE_URL set. Falling back to SQLite.")
    return "sqlite:///./oilquest.db"

DATABASE_URL = get_database_url()
print(f"Using Database URL: {DATABASE_URL}")

# SQLite requires specific connect_args
connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args["check_same_thread"] = False

engine = create_engine(DATABASE_URL, connect_args=connect_args)
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
