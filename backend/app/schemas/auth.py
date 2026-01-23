from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    email: str = Field(..., example="ana@email.com")
    password: str = Field(..., example="Senha@123")


class TokenResponse(BaseModel):
    token: str
