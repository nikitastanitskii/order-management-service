from src.Parts.repository.base_part_repository import BasePartsRepository
from src.Parts.repository.parts_repository import get_part_repository
from src.Parts.schemas.parts_schemas import PartModel
from fastapi import Depends
from pydantic import parse_obj_as


class GetAllParts:
    def __init__(self, part_repository: BasePartsRepository) -> None:
        self.__repository = part_repository

    def get_all(self) -> list[PartModel]:
        """Функция для получения списка всех запчастей"""
        all_parts = self.__repository.get_all()
        if not all_parts:
            return []
        return parse_obj_as(list[PartModel], all_parts)     # Преобразует необработанные данные в PartModel


def get_all_parts_service(
    part_repository: BasePartsRepository = Depends(get_part_repository),
) -> GetAllParts:
    return GetAllParts(part_repository=part_repository)
