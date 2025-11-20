from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

import socket
from dotenv import load_dotenv

load_dotenv()

def get_database_url():
    # 1. Prefer explicit env var (Required for Cloud Run)
    url = os.getenv("DATABASE_URL")
    if url:
        print(f"Found DATABASE_URL env var: {url}")
        return url
    
    print("DATABASE_URL env var not set.")

    # 2. Check if running in Cloud Run (K_SERVICE is set automatically)
    if os.getenv("K_SERVICE"):
        print("WARNING: Running in Cloud Run but DATABASE_URL is not set!")
        print("Please set DATABASE_URL in your Cloud Run service revision.")
        # Fallback to localhost might work if using Cloud SQL Auth Proxy sidecar, 
        # but usually this indicates a configuration error.
    
    # 3. Try to resolve 'db' host (Docker Compose)
    try:
        print("Attempting to resolve 'db' host...")
        socket.gethostbyname("db")
        print("'db' host resolved. Using docker connection.")
        return "postgresql://user:password@db:5432/oilquest"
    except socket.error:
        pass

    # 4. Fallback to localhost (Local development)
    print("Could not resolve 'db' host. Falling back to localhost.")
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
