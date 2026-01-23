from datetime import datetime

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str = Field(..., example="Ana")
    surname: str = Field(..., example="Silva")
    email: str = Field(..., example="ana@email.com")
    cpf: str = Field(..., example="123.456.789-00")
    password: str = Field(..., example="Senha@123")
    address: int | None = Field(default=None, example=1)
    is_active: bool = Field(default=True, example=True)
    is_verified: bool | None = Field(default=None, example=False)
    created_by: int | None = Field(default=None, example=10)
    updated_by: int | None = Field(default=None, example=10)
    last_login: datetime | None = None
    role: list[int] | None = Field(default=None, example=[1])


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: str | None = Field(default=None, example="Ana")
    surname: str | None = Field(default=None, example="Silva")
    email: str | None = Field(default=None, example="ana@email.com")
    cpf: str | None = Field(default=None, example="123.456.789-00")
    password: str | None = Field(default=None, example="Senha@123")
    address: int | None = Field(default=None, example=1)
    is_active: bool | None = Field(default=None, example=True)
    is_verified: bool | None = Field(default=None, example=False)
    updated_by: int | None = Field(default=None, example=10)
    last_login: datetime | None = None
    role: list[int] | None = Field(default=None, example=[1])


class UserRead(BaseModel):
    id: int
    name: str
    surname: str
    uuid: str
    email: str
    cpf: str
    password: str
    address: int | None
    is_active: bool
    is_verified: bool | None
    created_at: datetime
    updated_at: datetime
    created_by: int | None
    updated_by: int | None
    last_login: datetime | None
    role: list[int]

    class Config:
        from_attributes = True
