import csv
from sqlalchemy.orm import Session

from app.database import engine, SessionLocal, Base
from app.models import Estado, Municipio, Asentamiento
from app.crud import (  
    crear_estado,
    get_estado_por_nombre,
    crear_municipio,
    get_municipio_por_nombre_estado,
    crear_asentamiento
)

def init_db():
    # Elimina tablas si existen y las vuelve a crear
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def seed_data(csv_path: str):
    db: Session = SessionLocal()
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="|")
        for row in reader:
            d_estado = row[4].strip()
            d_mnpio = row[3].strip()
            d_asenta = row[1].strip()
            tipo = row[2].strip()
            zona = row[13].strip()
            cp = row[0].strip()

            # 1. Estado
            estado = get_estado_por_nombre(db, d_estado)
            if not estado:
                estado = crear_estado(db, d_estado)

            # 2. Municipio
            municipio = get_municipio_por_nombre_estado(db, d_mnpio, estado.id)
            if not municipio:
                municipio = crear_municipio(db, d_mnpio, estado.id)

            # 3. Asentamiento
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
