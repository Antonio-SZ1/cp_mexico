from fastapi import FastAPI
from app.database import engine, Base
from app.routers import codigos, estados, resumen

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Códigos Postales de México",
    description="Consulta de asentamientos por código postal",
    version="1.0.0"
)

app.include_router(codigos.router)
app.include_router(estados.router)
app.include_router(resumen.router)
