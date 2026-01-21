from sqlalchemy import Column, Integer, String

from app.core.database import Base


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    cep = Column(String(20), nullable=False)
    estado = Column(String(50), nullable=False)
    bairro = Column(String(100), nullable=False)
    tipo_logradouro = Column(String(100), nullable=False)
    logradouro = Column(String(200), nullable=False)
    numero = Column(String(50), nullable=False)
    complemento = Column(String(200), nullable=True)
    referencia = Column(String(200), nullable=True)
