import psycopg2
from src.core.settings import get_settings


def get_postgres_connector():
    """Функция для подключения к базе данных PostgreSQL"""
    settings = get_settings()
    return psycopg2.connect(
        database=settings.POSTGRES_DB,
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        host=settings.POSTGRES_HOST,
        port=settings.POSTGRES_PORT,
    )
