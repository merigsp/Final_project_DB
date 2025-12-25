from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.dialects.postgresql import JSONB

class Tournament(Base):
    __tablename__ = "tournear"
    
    tur_id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    city = Column(String(20), nullable=False)
    country = Column(String(20), nullable=False)
    t_name = Column(String(20), nullable=False)
    qualification_level = Column(Integer, nullable=False)
    
    participations = relationship("Participation", back_populates="tournament")
    additional_info = Column(JSONB, nullable=True)

class Participation(Base):
    __tablename__ = "participance"
    
    part_id = Column(Integer, primary_key=True, index=True)
    tur_id = Column(Integer, ForeignKey("tournear.tur_id"), nullable=False)
    start_number = Column(Integer, nullable=False)
    zanyatoye_mesto = Column(Integer, nullable=False)
    
    tournament = relationship("Tournament", back_populates="participations")
    player = relationship("Player", uselist=False, back_populates="participation")

class Player(Base):
    __tablename__ = "player"
    
    p_id = Column(Integer, primary_key=True, index=True)
    par_id = Column(Integer, ForeignKey("participance.part_id"), nullable=False)
    second_name = Column(String(20), nullable=False)
    country = Column(String(20), nullable=False)
    titul = Column(String(10), nullable=False)
    rating = Column(Integer, nullable=False)
    
    participation = relationship("Participation", back_populates="player")
