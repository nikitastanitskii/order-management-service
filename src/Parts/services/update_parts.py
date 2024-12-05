from fastapi import Depends
from src.Parts.repository.base_part_repository import BasePartsRepository
from src.Parts.repository.parts_repository import get_part_repository
from src.Parts.services.parts_exception import (
    PartsNotFoundException,
    PartNameCannotBeEmpty,
)
from src.Parts.schemas.parts_schemas import PartModel


class UpdateParts:
    def __init__(self, part_repository: BasePartsRepository) -> None:
        self.__repository = part_repository

    def update(self, part_id: int, part_data: PartModel) -> None:
        """Функция для обновления запчасти"""
        if not part_data.name:
            raise PartNameCannotBeEmpty("Название запчасти не может быть пустым.")
        existing_part = self.__repository.get(part_id)
        if not existing_part:
            raise PartsNotFoundException(f"Запчасть с ID {part_id} не найдена.")

        # Обновляем запчасть
        self.__repository.update(part_id, part_data)
        return None


def get_update_parts_service(
    part_repository: BasePartsRepository = Depends(get_part_repository),
) -> UpdateParts:
    return UpdateParts(part_repository=part_repository)
