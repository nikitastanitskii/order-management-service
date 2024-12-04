from src.Parts.repository.base_part_repository import BasePartsRepository
from src.Parts.repository.parts_repository import get_part_repository
from src.Parts.schemas.parts_schemas import PartModel
from fastapi import Depends


class GetAllParts:
    def __init__(self, part_repository: BasePartsRepository) -> None:
        self.__repository = part_repository

    def get_all(self) -> list[PartModel]:
        return self.__repository.get_all()


def get_all_parts_service(
    part_repository: BasePartsRepository = Depends(get_part_repository),
) -> GetAllParts:
    return GetAllParts(part_repository=part_repository)
