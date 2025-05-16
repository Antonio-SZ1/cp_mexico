import os
import csv
import traceback
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
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def seed_data(csv_path: str):
    # 1) Comprobar existencia
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"No se encontró el CSV en: {csv_path}")

    db: Session = SessionLocal()
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="|")
        for idx, row in enumerate(reader, start=1):
            try:
                if not row or len(row) < 14:
                    print(f"Fila {idx}: saltada (longitud {len(row)})")
                    continue

                d_estado  = row[4].strip()
                d_mnpio   = row[3].strip()
                d_asenta  = row[1].strip()
                tipo      = row[2].strip()
                zona      = row[13].strip()
                cp        = row[0].strip()

                # 2) Estado
                estado = get_estado_por_nombre(db, d_estado)
                if not estado:
                    estado = crear_estado(db, d_estado)
                    db.commit()
                    print(f"  > Estado creado: {d_estado}")

                # 3) Municipio
                municipio = get_municipio_por_nombre_estado(db, d_mnpio, estado.id)
                if not municipio:
                    municipio = crear_municipio(db, d_mnpio, estado.id)
                    db.commit()
                    print(f"  > Municipio creado: {d_mnpio} (estado {d_estado})")

                # 4) Asentamiento
                crear_asentamiento(
                    db,
                    nombre=d_asenta,
                    tipo=tipo,
                    zona=zona,
                    cp=cp,
                    municipio_id=municipio.id
                )
                db.commit()
                print(f"  > Asentamiento creado [{cp}]: {d_asenta}")

            except Exception:
                print(f"⚠️ Error en fila {idx}:")
                traceback.print_exc()
                # decide si quieres continuar o abortar
                # break
    db.close()

if __name__ == "__main__":
    try:
        print("Inicializando DB...")
        init_db()
        print("Sembrando datos...")
        seed_data("data/codigos_postales.csv")
        print("✅ ¡Datos seed cargados con éxito!")
    except Exception:
        print("🚨 Error durante el seed:")
        traceback.print_exc()
        exit(1)
