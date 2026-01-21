from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    project_name: str = "Meu Mundinho Feliz API"
    database_url: str

    class Config:
        env_file = ".env"


settings = Settings()
