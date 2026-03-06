from sqlalchemy import Boolean, Column, Integer, String
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)
    puntos_totales = Column(Integer, default=0)

class Prediccion(Base):
    __tablename__ = "predicciones"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    datos = Column(String) # Guardaremos el JSON serializado por ahora para migrar rápido

class ConfigGlobal(Base):
    __tablename__ = "config_global"

    id = Column(Integer, primary_key=True, index=True)
    clave = Column(String, unique=True, index=True)
    valor = Column(String) # JSON serializado (ej: el estado de las fases)

class DatosOficiales(Base):
    __tablename__ = "datos_oficiales"

    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(String, unique=True, index=True)
    datos = Column(String) # Goles, ganador, penales, etc.

class Premio(Base):
    __tablename__ = "premios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    descripcion = Column(String)
    puntos_requeridos = Column(Integer, default=0)
    imagen_url = Column(String) # Rango de imagen: /static/premios/1.jpg
    orden = Column(Integer, default=0) # Para ordenar en la UI
