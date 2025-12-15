from pydantic import BaseModel
from datetime import date
from typing import Optional, List

# Tournament schemas
class TournamentBase(BaseModel):
    date: date
    city: str
    country: str
    t_name: str
    qualification_level: int

class TournamentCreate(TournamentBase):
    pass

class Tournament(TournamentBase):
    tur_id: int
    
    class Config:
        from_attributes = True

# Participation schemas
class ParticipationBase(BaseModel):
    tur_id: int
    start_number: int
    zanyatoye_mesto: int

class ParticipationCreate(ParticipationBase):
    pass

class Participation(ParticipationBase):
    part_id: int
    
    class Config:
        from_attributes = True

# Player schemas
class PlayerBase(BaseModel):
    par_id: int
    second_name: str
    country: str
    titul: str
    rating: int

class PlayerCreate(PlayerBase):
    pass

class Player(PlayerBase):
    p_id: int
    
    class Config:
        from_attributes = True

# Response schemas
class TournamentWithParticipants(Tournament):
    participations: List[Participation] = []

class ParticipationWithDetails(Participation):
    tournament: Optional[Tournament] = None
    player: Optional[Player] = None
