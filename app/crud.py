from sqlalchemy.orm import Session
from . import models

def crear_estado(db: Session, nombre: str):
    obj = models.Estado(nombre=nombre)
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def get_estado_por_nombre(db: Session, nombre: str):
    return db.query(models.Estado).filter_by(nombre=nombre).first()

def crear_municipio(db: Session, nombre: str, estado_id: int):
    obj = models.Municipio(nombre=nombre, estado_id=estado_id)
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def get_municipio_por_nombre_estado(db: Session, nombre: str, estado_id: int):
    return db.query(models.Municipio)\
             .filter_by(nombre=nombre, estado_id=estado_id)\
             .first()

def crear_asentamiento(db: Session, nombre, tipo, zona, cp, municipio_id: int):
    obj = models.Asentamiento(
        nombre=nombre,
        tipo_asentamiento=tipo,
        zona=zona,
        codigo_postal=cp,
        municipio_id=municipio_id
    )
    db.add(obj); db.commit(); db.refresh(obj)
    return obj
