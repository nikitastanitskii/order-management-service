from fastapi import Depends
from src.Supplies.repository.base_supplies_repository import BaseSuppliesRepository
from src.Supplies.repository.supplies_repository import get_supplies_repository
from src.Supplies.schemas.supplies_schemas import SuppliesModel
from src.Supplies.services.supplies_exception import SuppliesNameCannotBeEmpty, SuppliesAndPartNameCannotBeEmpty


class CreateSupplies:
    def __init__(self, supply_repository: BaseSuppliesRepository) -> None:
        self.__repository = supply_repository

    def create(self, supplies_data: SuppliesModel) -> None:
        """Функция для создания поставки"""
        if not supplies_data.part_id or not supplies_data.supplier_id:
            raise SuppliesAndPartNameCannotBeEmpty(
                "ID запчасти и поставщика обязательны для создания поставки."
            )
        self.__repository.create(supplies_data)


def get_create_supply_service(
    supply_repository: BaseSuppliesRepository = Depends(get_supplies_repository),
) -> CreateSupplies:
    return CreateSupplies(supply_repository=supply_repository)
