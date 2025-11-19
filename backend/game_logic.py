import random
from sqlalchemy.orm import Session
from models import Acreage, GameState, AcreageStatus

# Simple grid settings
LAT_START = 50.0
LAT_END = 60.0
LON_START = 0.0
LON_END = 10.0
STEP = 0.5

def initialize_world(db: Session):
    # Check if world exists
    if db.query(Acreage).first():
        return {"message": "World already initialized"}

    # Create Game State
    game_state = GameState(turn_number=1)
    db.add(game_state)

    # Generate Grid
    lat = LAT_START
    count = 0
    while lat < LAT_END:
        lon = LON_START
        while lon < LON_END:
            # Simple noise: random for now, can improve later
            potential = random.random() 
            
            acreage = Acreage(
                lat=lat,
                lon=lon,
                oil_potential=potential,
                status=AcreageStatus.AVAILABLE
            )
            db.add(acreage)
            lon += STEP
            count += 1
        lat += STEP
    
    db.commit()
    return {"message": f"World initialized with {count} acreages"}

def get_map_data(db: Session):
    acreages = db.query(Acreage).all()
    return [
        {
            "id": a.id,
            "lat": a.lat,
            "lon": a.lon,
            "owner_id": a.owner_id,
            "status": a.status,
            # Hide oil_potential
        }
        for a in acreages
    ]
