from fastapi import Depends
from src.Supplies.repository.base_supplies_repository import BaseSuppliesRepository
from src.Supplies.repository.supplies_repository import get_supplies_repository
from src.Supplies.schemas.supplies_schemas import SuppliesModel


class GetAllSupplies:
    def __init__(self, supply_repository: BaseSuppliesRepository) -> None:
        self.__repository = supply_repository

    def get_all(self) -> list[SuppliesModel]:
        """Функция для получения списка всех поставок"""
        return self.__repository.get_all()


def get_all_supplies_service(
    supply_repository: BaseSuppliesRepository = Depends(get_supplies_repository),
) -> GetAllSupplies:
    return GetAllSupplies(supply_repository=supply_repository)
