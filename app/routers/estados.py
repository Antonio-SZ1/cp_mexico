from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Estado, Municipio

router = APIRouter(prefix="/api")

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.get("/estados")
def obtener_estados(db: Session = Depends(get_db)):
    return db.query(Estado).all()

@router.get("/municipios")
def obtener_municipios(estado_id: int, db: Session = Depends(get_db)):
    return db.query(Municipio).filter_by(estado_id=estado_id).all()
