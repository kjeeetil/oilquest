from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import models
import game_logic

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="OilQuest API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to OilQuest API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/admin/init")
def init_world(db: Session = Depends(get_db)):
    return game_logic.initialize_world(db)

@app.get("/map")
def get_map(db: Session = Depends(get_db)):
    return game_logic.get_map_data(db)

