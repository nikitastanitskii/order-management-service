from fastapi import Depends
from src.Supplies.repository.base_supplies_repository import BaseSuppliesRepository
from src.Supplies.repository.supplies_repository import get_supplies_repository
from src.Supplies.services.supplies_exception import SuppliesNameCannotBeEmpty


class DeleteSupplies:
    def __init__(self, supplies_repository: BaseSuppliesRepository) -> None:
        self.__repository = supplies_repository

    def delete(self, supplies_id: int) -> None:
        if not supplies_id:
            raise SuppliesNameCannotBeEmpty("ID поставки обязателен для удаления.")
        self.__repository.delete(supplies_id)


def get_delete_supply_service(
    supplies_repository: BaseSuppliesRepository = Depends(get_supplies_repository),
) -> DeleteSupplies:
    return DeleteSupplies(supplies_repository=supplies_repository)
