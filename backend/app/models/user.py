from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Text, func
from sqlalchemy.dialects.postgresql import ARRAY

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)
    uuid = Column(Text, nullable=False)
    token = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    cpf = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    address = Column(Integer, ForeignKey("address.id"), nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
    is_verified = Column(Boolean, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
    last_login = Column(DateTime(timezone=True), nullable=True)
    role = Column(ARRAY(Integer), nullable=False, default=list)
