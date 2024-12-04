from fastapi import Depends
from src.Supplies.repository.base_supplies_repository import BaseSuppliesRepository
from src.Supplies.repository.supplies_repository import get_supplies_repository


class DeleteSupplies:
    def __init__(self, supplies_repository: BaseSuppliesRepository) -> None:
        self.__repository = supplies_repository

    def delete(self, supplies_id: int) -> None:
        if not supplies_id:
            raise ValueError("ID поставки обязателен для удаления.")
        self.__repository.delete(supplies_id)


def get_delete_supply_service(
    supply_repository: BaseSuppliesRepository = Depends(get_supplies_repository),
) -> DeleteSupplies:
    return DeleteSupplies(supply_repository=supply_repository)