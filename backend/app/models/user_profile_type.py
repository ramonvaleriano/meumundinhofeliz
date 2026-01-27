from sqlalchemy import Column, ForeignKey, Integer

from app.core.database import Base


class UserProfileType(Base):
    __tablename__ = "user_profile_type"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    profile_type_id = Column(
        Integer, ForeignKey("profile_type.id", ondelete="CASCADE"), nullable=False
    )
