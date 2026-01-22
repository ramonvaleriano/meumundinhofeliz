import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    def __init__(self) -> None:
        self.project_name = os.getenv("PROJECT_NAME", "Meu Mundinho Feliz API")
        self.database_url = os.getenv("DATABASE_URL")
        self.crypto_key = os.getenv("CRYPTO_KEY")
        if not self.database_url:
            raise ValueError("DATABASE_URL nao definido")

    @property
    def database_url_sync(self) -> str:
        if "+asyncpg" in self.database_url:
            return self.database_url.replace("+asyncpg", "+psycopg2")
        return self.database_url


settings = Settings()
