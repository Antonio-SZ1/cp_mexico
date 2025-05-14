from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import SessionLocal
from app.models import Asentamiento

router = APIRouter(prefix="/api")

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.get("/resumen-zona")
def resumen_zona(cp: str, db: Session = Depends(get_db)):
    return db.query(
        Asentamiento.zona,
        func.count(Asentamiento.id).label("cantidad")
    ).filter_by(codigo_postal=cp).group_by(Asentamiento.zona).all()
