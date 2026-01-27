from pydantic import BaseModel, Field


class UserProfileTypeBase(BaseModel):
    user_id: int = Field(..., example=1)
    profile_type_id: int = Field(..., example=2)


class UserProfileTypeCreate(UserProfileTypeBase):
    pass


class UserProfileTypeUpdate(BaseModel):
    user_id: int | None = Field(default=None, example=1)
    profile_type_id: int | None = Field(default=None, example=2)


class UserProfileTypeRead(UserProfileTypeBase):
    id: int

    class Config:
        from_attributes = True
