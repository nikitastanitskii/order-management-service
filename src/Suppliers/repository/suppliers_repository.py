from src.Suppliers.repository.base_suppliers_repository import BaseSuppliersRepository
from src.Suppliers.schemas.suppliers_schemas import SuppliersModel
from fastapi import Depends
from src.core.db.postgres_connector import get_postgres_connector


class SuppliersRepository(BaseSuppliersRepository):
    def __init__(self, connector):  # Подключение к базе данных
        self.__connector = connector

    def create(self, suppliers_data: SuppliersModel) -> None:
        """Создание нового поставщика"""
        with self.__connector:
            with self.__connector.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO suppliers (name, contact)
                    VALUES (%s, %s);
                    """,
                    (suppliers_data.name, suppliers_data.contact),
                )

    def get_all(self) -> list[SuppliersModel]:
        """Получение списка всех поставщиков"""
        with self.__connector:
            with self.__connector.cursor() as cursor:
                cursor.execute("SELECT * FROM suppliers;")
                rows = cursor.fetchall()
                return [
                    SuppliersModel(
                        id=row[0],
                        name=row[1],
                        contact=row[2],
                    )
                    for row in rows
                ]

    def update(self, supplier_id: int, suppliers_data: SuppliersModel) -> None:
        """Обновление данных поставщика по ID"""
        with self.__connector:
            with self.__connector.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE suppliers
                    SET name = %s, contact = %s
                    WHERE id = %s;
                    """,
                    (
                        suppliers_data.name,
                        suppliers_data.contact,
                        supplier_id,
                    ),
                )

    def delete(self, supplier_id: int) -> bool:
        """Удаление поставщика по ID"""
        with self.__connector:
            with self.__connector.cursor() as cursor:
                cursor.execute("DELETE FROM suppliers WHERE id = %s;", (supplier_id,))
        return True

    def get(self, supplier_id: int) -> SuppliersModel:
        """Получение данных запчасти по ID"""
        with self.__connector:
            with self.__connector.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, name, contact
                    FROM suppliers
                    WHERE id = %s;
                    """,
                    (supplier_id,),
                )
                result = cursor.fetchone()  # Получаем одну запись

                # Возвращаем данные в виде модели PartModel
                return SuppliersModel(id=result[0], name=result[1], contact=result[2])


def get_suppliers_repository(
    connector=Depends(get_postgres_connector),
) -> BaseSuppliersRepository:
    return SuppliersRepository(connector=connector)
