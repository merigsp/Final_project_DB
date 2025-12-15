from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
import crud, models, schemas
from database import SessionLocal, engine

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tournament Management API")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Tournament Management API"}

# Tournament endpoints
@app.post("/tournaments/", response_model=schemas.Tournament)
def create_tournament(tournament: schemas.TournamentCreate, db: Session = Depends(get_db)):
    return crud.create_tournament(db=db, tournament=tournament)

@app.get("/tournaments/", response_model=List[schemas.Tournament])
def read_tournaments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tournaments = crud.get_tournaments(db, skip=skip, limit=limit)
    return tournaments

@app.get("/tournaments/{tournament_id}", response_model=schemas.Tournament)
def read_tournament(tournament_id: int, db: Session = Depends(get_db)):
    db_tournament = crud.get_tournament(db, tournament_id=tournament_id)
    if db_tournament is None:
        raise HTTPException(status_code=404, detail="Tournament not found")
    return db_tournament

@app.put("/tournaments/{tournament_id}", response_model=schemas.Tournament)
def update_tournament(tournament_id: int, tournament: schemas.TournamentCreate, db: Session = Depends(get_db)):
    return crud.update_tournament(db=db, tournament_id=tournament_id, tournament_update=tournament)

@app.delete("/tournaments/{tournament_id}")
def delete_tournament(tournament_id: int, db: Session = Depends(get_db)):
    crud.delete_tournament(db=db, tournament_id=tournament_id)
    return {"message": "Tournament deleted"}

# Participation endpoints
@app.post("/participations/", response_model=schemas.Participation)
def create_participation(participation: schemas.ParticipationCreate, db: Session = Depends(get_db)):
    return crud.create_participation(db=db, participation=participation)

# Player endpoints
@app.post("/players/", response_model=schemas.Player)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    return crud.create_player(db=db, player=player)

