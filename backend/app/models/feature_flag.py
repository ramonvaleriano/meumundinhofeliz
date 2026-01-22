from sqlalchemy import Boolean, Column, DateTime, Integer, Text, func

from app.core.database import Base


class FeatureFlag(Base):
    __tablename__ = "feature_flag"

    id = Column(Integer, primary_key=True, index=True)
    name_flag = Column(Text, nullable=False)
    is_enabled = Column(Boolean, nullable=False, default=True)
    status = Column(Text, nullable=True)
    strategy = Column(Text, nullable=False)
    variation = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
