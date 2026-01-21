from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    project_name: str = "Meu Mundinho Feliz API"
    database_url: str

    class Config:
        env_file = ".env"

    @property
    def database_url_sync(self) -> str:
        if "+asyncpg" in self.database_url:
            return self.database_url.replace("+asyncpg", "+psycopg2")
        return self.database_url


settings = Settings()
