from fastapi import Depends
from src.Supplies.repository.base_supplies_repository import BaseSuppliesRepository
from src.Supplies.repository.supplies_repository import get_supplies_repository
from src.Supplies.schemas.supplies_schemas import SuppliesModel
from src.Supplies.services.supplies_exception import SuppliesNameCannotBeEmpty


class UpdateSupplies:
    def __init__(self, supply_repository: BaseSuppliesRepository) -> None:
        self.__repository = supply_repository

    def update(self, supply_id: int, supply_data: SuppliesModel) -> None:
        """Функция для обновления данных о поставке"""
        if not supply_id:
            raise SuppliesNameCannotBeEmpty("ID поставки обязателен для обновления.")
        self.__repository.update(supply_id, supply_data)


def get_update_supply_service(
    supply_repository: BaseSuppliesRepository = Depends(get_supplies_repository),
) -> UpdateSupplies:
    return UpdateSupplies(supply_repository=supply_repository)
