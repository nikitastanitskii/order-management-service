from src.Parts.repository.base_part_repository import BasePartsRepository
from src.Parts.repository.parts_repository import get_part_repository
from src.Parts.services.parts_exception import PartNameCannotBeEmpty, PartsAlreadyExists
from src.Parts.schemas.parts_schemas import PartModel
from fastapi import Depends


class CreateParts:
    def __init__(self, part_repository: BasePartsRepository) -> None:
        self.__repository = part_repository

    def create(self, part_data: PartModel) -> None:
        if not part_data.name:
            raise PartNameCannotBeEmpty("Название запчасти не может быть пустым.")
        # Проверка, что такая запчасть уже существует
        if self.__repository.exists(part_data.name):
            raise PartsAlreadyExists(f"Запчасть с названием {part_data.name} уже существует.")

        self.__repository.create(part_data)


def get_create_parts_service(
    part_repository: BasePartsRepository = Depends(get_part_repository),
) -> CreateParts:
    return CreateParts(part_repository=part_repository)
