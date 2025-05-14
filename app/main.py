from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database import engine, Base
from app.routers import codigos, estados, resumen


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Códigos Postales de México",
    description="Consulta de asentamientos por código postal",
    version="1.0.0"
)


app.mount("/", StaticFiles(directory="static", html=True), name="static")


app.include_router(codigos.router)
app.include_router(estados.router)
app.include_router(resumen.router)
