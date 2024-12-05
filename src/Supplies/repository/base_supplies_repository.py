from abc import ABC, abstractmethod
from src.Supplies.schemas.supplies_schemas import SuppliesModel


class BaseSuppliesRepository(ABC):
    @abstractmethod
    def create(self, supplies_data: SuppliesModel) -> None:
        pass

    @abstractmethod
    def get_all(self) -> list[SuppliesModel]:
        pass

    @abstractmethod
    def update(self, supplies_id: int, supplies_data: SuppliesModel) -> None:
        pass

    @abstractmethod
    def delete(self, supplies_id: int) -> bool:
        pass
