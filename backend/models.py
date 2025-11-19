from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from database import Base

class AcreageStatus(str, enum.Enum):
    AVAILABLE = "AVAILABLE"
    OWNED = "OWNED"
    EXPLORED = "EXPLORED"
    PRODUCING = "PRODUCING"

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    cash = Column(Float, default=1000000.0)
    color = Column(String, default="#0000FF")
    
    acreages = relationship("Acreage", back_populates="owner")

class Acreage(Base):
    __tablename__ = "acreages"

    id = Column(Integer, primary_key=True, index=True)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    owner_id = Column(Integer, ForeignKey("players.id"), nullable=True)
    oil_potential = Column(Float, default=0.0) # Hidden from user until explored
    status = Column(String, default=AcreageStatus.AVAILABLE)
    
    owner = relationship("Player", back_populates="acreages")

class GameState(Base):
    __tablename__ = "gamestate"

    id = Column(Integer, primary_key=True, index=True)
    turn_number = Column(Integer, default=1)
    last_processed = Column(String, nullable=True)
