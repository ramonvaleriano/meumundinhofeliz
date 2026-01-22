from datetime import datetime

from pydantic import BaseModel, Field


class FeatureFlagBase(BaseModel):
    name_flag: str = Field(..., example="habilitar_novo_formulario")
    is_enabled: bool = Field(default=True, example=True)
    status: str | None = Field(default=None, example="beta")
    strategy: str = Field(
        ..., example="liberar_para_grupo_a; rollout=25%; regra: idade>=5"
    )
    variation: str | None = Field(default=None, example="A")
    created_by: int | None = Field(default=None, example=10)
    updated_by: int | None = Field(default=None, example=10)


class FeatureFlagCreate(FeatureFlagBase):
    pass


class FeatureFlagUpdate(BaseModel):
    name_flag: str | None = Field(default=None, example="habilitar_novo_formulario")
    is_enabled: bool | None = Field(default=None, example=True)
    status: str | None = Field(default=None, example="stable")
    strategy: str | None = Field(
        default=None, example="liberar_para_todos; rollout=100%"
    )
    variation: str | None = Field(default=None, example="B")
    updated_by: int | None = Field(default=None, example=10)


class FeatureFlagRead(FeatureFlagBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
