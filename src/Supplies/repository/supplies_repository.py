from src.Supplies.repository.base_supplies_repository import BaseSuppliesRepository
from src.Supplies.schemas.Supplies_schemas import SuppliesModel
from fastapi import Depends
from src.core.db.postgres_connector import get_postgres_connector


class SuppliesRepository(BaseSuppliesRepository):
    def __init__(self, connector):  # Подключение к базе данных
        self.__connector = connector

    def create(self, supplies_data: SuppliesModel) -> None:
        """Создание новой поставки"""
        with self.__connector:
            with self.__connector.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO supplies (part_id, supplier_id, quantity, date)
                    VALUES (%s, %s, %s, %s);
                    """,
                    (
                        supplies_data.part_id,
                        supplies_data.supplier_id,
                        supplies_data.quantity,
                        supplies_data.date,
                    ),
                )

    def get_all(self) -> list[SuppliesModel]:
        """Получение списка всех поставок"""
        with self.__connector:
            with self.__connector.cursor() as cursor:
                cursor.execute("SELECT * FROM supplies;")
                rows = cursor.fetchall()
                return [
                    SuppliesModel(
                        part_id=row[0],
                        supplier_id=row[1],
                        quantity=row[2],
                        date=row[3],
                    )
                    for row in rows
                ]

    def update(self, supplies_id: int, supplies_data: SuppliesModel) -> None:
        """Обновление данных поставки по ID"""
        with self.__connector:
            with self.__connector.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE supplies
                    SET part_id = %s, supplier_id = %s, quantity = %s, date = %s
                    WHERE id = %s;
                    """,
                    (
                        supplies_data.part_id,
                        supplies_data.supplier_id,
                        supplies_data.quantity,
                        supplies_data.date,
                        supplies_id,
                    ),
                )

    def delete(self, supplies_id: int):
        """Удаление поставки по ID."""
        with self.__connector:
            with self.__connector.cursor() as cursor:
                cursor.execute("DELETE FROM supplies WHERE id = %s;", (supplies_id,))
        return True


def get_supplies_repository(
    connector=Depends(get_postgres_connector),
) -> BaseSuppliesRepository:
    return SuppliesRepository(connector=connector)
