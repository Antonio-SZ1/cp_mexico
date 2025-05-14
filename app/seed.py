import csv
from sqlalchemy.orm import Session

from app.database import engine, SessionLocal, Base
from app.models import Estado, Municipio, Asentamiento
from app.crud import (  # type: ignore
    crear_estado,
    get_estado_por_nombre,
    crear_municipio,
    get_municipio_por_nombre_estado,
    crear_asentamiento
)

def init_db():
   
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def seed_data(csv_path: str):
    db: Session = SessionLocal()
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="|")
        for idx, row in enumerate(reader, start=1):
          
            if not row or len(row) < 14:
                
                continue

            d_estado  = row[4].strip()
            d_mnpio   = row[3].strip()
            d_asenta  = row[1].strip()
            tipo      = row[2].strip()
            zona      = row[13].strip()
            cp        = row[0].strip()

         
            estado = get_estado_por_nombre(db, d_estado)
            if not estado:
                estado = crear_estado(db, d_estado)

         
            municipio = get_municipio_por_nombre_estado(db, d_mnpio, estado.id)
            if not municipio:
                municipio = crear_municipio(db, d_mnpio, estado.id)

           
            crear_asentamiento(
                db,
                nombre=d_asenta,
                tipo=tipo,
                zona=zona,
                cp=cp,
                municipio_id=municipio.id
            )
    db.close()

if __name__ == "__main__":
    init_db()
    seed_data("data/codigos_postales.csv")
    print("¡Datos seed cargados con éxito!")
