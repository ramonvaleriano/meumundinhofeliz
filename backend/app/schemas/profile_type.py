from pydantic import BaseModel, Field


class ProfileTypeBase(BaseModel):
    user_type: str = Field(..., example="Neuropediatra")


class ProfileTypeCreate(ProfileTypeBase):
    pass


class ProfileTypeUpdate(BaseModel):
    user_type: str | None = Field(default=None, example="Neuropediatra")


class ProfileTypeRead(ProfileTypeBase):
    id: int

    class Config:
        from_attributes = True
