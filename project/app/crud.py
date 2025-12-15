from sqlalchemy.orm import Session
from sqlalchemy import and_
from models import Tournament, Participation, Player
import schemas

# Tournament CRUD
def get_tournament(db: Session, tournament_id: int):
    return db.query(Tournament).filter(Tournament.tur_id == tournament_id).first()

def get_tournaments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Tournament).offset(skip).limit(limit).all()

def create_tournament(db: Session, tournament: schemas.TournamentCreate):
    db_tournament = Tournament(**tournament.model_dump())
    db.add(db_tournament)
    db.commit()
    db.refresh(db_tournament)
    return db_tournament

def update_tournament(db: Session, tournament_id: int, tournament_update: schemas.TournamentCreate):
    db_tournament = get_tournament(db, tournament_id)
    if db_tournament:
        for key, value in tournament_update.model_dump().items():
            setattr(db_tournament, key, value)
        db.commit()
        db.refresh(db_tournament)
    return db_tournament

def delete_tournament(db: Session, tournament_id: int):
    db_tournament = get_tournament(db, tournament_id)
    if db_tournament:
        db.delete(db_tournament)
        db.commit()
    return db_tournament

# Participation CRUD
def create_participation(db: Session, participation: schemas.ParticipationCreate):
    db_participation = Participation(**participation.model_dump())
    db.add(db_participation)
    db.commit()
    db.refresh(db_participation)
    return db_participation

def get_participation(db: Session, participation_id: int):
    return db.query(Participation).filter(Participation.part_id == participation_id).first()

# Player CRUD
def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = Player(**player.model_dump())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def get_player(db: Session, player_id: int):
    return db.query(Player).filter(Player.p_id == player_id).first()
