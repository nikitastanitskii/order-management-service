from src.Parts.repository.base_part_repository import BasePartsRepository
from fastapi import Depends
from src.Parts.repository.parts_repository import get_part_repository
from src.Parts.services.parts_exception import PartsNotFoundException


class DeleteParts:
    def __init__(self, part_repository: BasePartsRepository) -> None:
        self.__repository = part_repository

    def delete(self, part_id: int) -> None:
        """Функция для удаления запчасти"""
        # Проверяем, существует ли запчасть
        if self.__repository.get(part_id):
            self.__repository.delete(part_id)
        else:
            raise PartsNotFoundException(f"Запчасть с ID {part_id} не найдена.")


def get_delete_parts_service(
    part_repository: BasePartsRepository = Depends(get_part_repository),
) -> DeleteParts:
    return DeleteParts(part_repository=part_repository)
