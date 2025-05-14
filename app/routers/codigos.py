from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Asentamiento

router = APIRouter(prefix="/api")

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.get("/codigo")
def obtener_por_cp(cp: str, db: Session = Depends(get_db)):
    lista = db.query(Asentamiento).filter_by(codigo_postal=cp).all()
    if not lista:
        raise HTTPException(404, f"No se encontraron asentamientos para CP {cp}")
    return lista
