from src.Parts.repository.base_part_repository import BasePartsRepository
from fastapi import Depends
from src.Parts.schemas.parts_schemas import PartModel
from src.core.db.postgres_connector import get_postgres_connector


class PartsRepository(BasePartsRepository):
    def __init__(self, connector):  # Подключение к базе данных
        self.__connector = connector

    def exists(self, name: str) -> bool:
        """Проверка, существует ли запчасть с таким названием"""
        with self.__connector:
            with self.__connector.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT 1 FROM parts WHERE name = %s LIMIT 1;
                    """,
                    (name,),
                )
                return cursor.fetchone() is not None

    def create(self, part_data: PartModel) -> None:
        """Создание запчасти"""
        with self.__connector:
            with self.__connector.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO parts (name, description, price, in_stock)
                    VALUES (%s, %s, %s, %s);
                    """,
                    (
                        part_data.name,
                        part_data.description,
                        part_data.price,
                        part_data.in_stock,
                    ),
                )

    def get_all(self) -> list[PartModel]:
        """Получение списка всех запчастей"""
        with self.__connector:
            with self.__connector.cursor() as cursor:
                cursor.execute("SELECT * FROM parts;")
                rows = cursor.fetchall()
                return [
                    PartModel(
                        id=row[0],
                        name=row[1],
                        description=row[2],
                        price=row[3],
                        in_stock=row[4],
                    )
                    for row in rows
                ]

    def update(self, part_id: int, part_data: PartModel) -> None:
        """Обновление данных запчасти по ID"""
        with self.__connector:
            with self.__connector.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE parts
                    SET name = %s, description = %s, price = %s, in_stock = %s
                    WHERE id = %s;
                """,
                    (
                        part_data.name,
                        part_data.description,
                        part_data.price,
                        part_data.in_stock,
                        part_id,
                    ),
                )

    def delete(self, part_id: int) -> bool:
        """Удаление запчасти по ID с проверкой существования"""
        with self.__connector:
            with self.__connector.cursor() as cursor:
                # Удаляем запчасть, если она существует
                cursor.execute(
                    """
                    DELETE FROM parts WHERE id = %s;
                    """,
                    (part_id,),
                )
            return True

    def get(self, part_id: int) -> PartModel:
        """Получение данных запчасти по ID"""
        with self.__connector:
            with self.__connector.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, name, description, price, in_stock
                    FROM parts
                    WHERE id = %s;
                    """,
                    (part_id,),
                )
                result = cursor.fetchone()  # Получаем одну запись

                # Возвращаем данные в виде модели PartModel
                return PartModel(
                    id=result[0],
                    name=result[1],
                    description=result[2],
                    price=result[3],
                    in_stock=result[4],
                )


def get_part_repository(
    connector=Depends(get_postgres_connector),
) -> BasePartsRepository:
    return PartsRepository(connector=connector)
