from abc import ABC, abstractmethod
from src.Suppliers.schemas.Suppliers_schemas import SuppliersModel


class BaseSuppliersRepository(ABC):
    @abstractmethod
    def create(self, supplies_data: SuppliersModel) -> None:
        pass

    @abstractmethod
    def get_all(self) -> list[SuppliersModel]:
        pass

    @abstractmethod
    def update(self, supplies_id: int, supplies_data: SuppliersModel) -> None:
        pass

    @abstractmethod
    def delete(self, supplies_id: int) -> bool:
        pass

    @abstractmethod
    def get(self, supplies_id: int) -> SuppliersModel:
        pass
