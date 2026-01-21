from sqlalchemy import Column, Integer, String

from app.core.database import Base


class ProfileType(Base):
    __tablename__ = "profile_type"

    id = Column(Integer, primary_key=True, index=True)
    user_type = Column(String(100), nullable=False)
