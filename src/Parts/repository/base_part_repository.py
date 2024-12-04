from abc import ABC, abstractmethod
from src.Parts.schemas.parts_schemas import PartModel


class BasePartsRepository(ABC):

    @abstractmethod
    def exists(self, name: str) -> bool:
        pass

    @abstractmethod
    def create(self, part_data: PartModel) -> None:
        pass

    @abstractmethod
    def get_all(self) -> list[PartModel]:
        pass

    @abstractmethod
    def update(self, part_id: int, part_data: PartModel) -> None:
        pass

    @abstractmethod
    def delete(self, part_id: int) -> bool:
        pass

    @abstractmethod
    def get(self, part_id: int) -> PartModel:
        pass
