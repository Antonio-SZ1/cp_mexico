import csv
from sqlalchemy.orm import Session
from .database import engine, SessionLocal, Base
from .models import Estado, Municipio, Asentamiento
from .crud import ( # type: ignore
    crear_estado, get_estado_por_nombre,
    crear_municipio, get_municipio_por_nombre_estado,
    crear_asentamiento
)

def init_db():
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

            # Estado
            estado = get_estado_por_nombre(db, d_estado)
            if not estado:
                estado = crear_estado(db, d_estado)

            # Municipio
            municipio = get_municipio_por_nombre_estado(db, d_mnpio, estado.id)
            if not municipio:
                municipio = crear_municipio(db, d_mnpio, estado.id)

            # Asentamiento
            crear_asentamiento(
                db, d_asenta, tipo, zona, cp, municipio.id
            )
    db.close()

if __name__ == "__main__":
    init_db()
    seed_data("data/codigos_postales.csv")
    print("¡Datos seed cargados con éxito!")
