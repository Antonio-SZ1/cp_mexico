from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Estado(Base):
    __tablename__ = "estados"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    municipios = relationship("Municipio", back_populates="estado")

class Municipio(Base):
    __tablename__ = "municipios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    estado_id = Column(Integer, ForeignKey("estados.id"))
    estado = relationship("Estado", back_populates="municipios")
    asentamientos = relationship("Asentamiento", back_populates="municipio")

class Asentamiento(Base):
    __tablename__ = "asentamientos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    tipo_asentamiento = Column(String)
    zona = Column(String)
    codigo_postal = Column(String, index=True)
    municipio_id = Column(Integer, ForeignKey("municipios.id"))
    municipio = relationship("Municipio", back_populates="asentamientos")
