from fastapi import Depends, APIRouter, HTTPException
from src.Parts.services.create_parts import CreateParts, get_create_parts_service
from src.Parts.services.delete_parts import DeleteParts, get_delete_parts_service
from src.Parts.services.get_all_parts import GetAllParts, get_all_parts_service
from src.Parts.services.parts_exception import (
    PartsAlreadyExists,
    PartsNotFoundException,
)
from src.Parts.schemas.parts_schemas import PartModel
from src.Parts.services.update_parts import UpdateParts, get_update_parts_service

parts_router = APIRouter(prefix="/parts")


@parts_router.post("/", summary="Метод для создания запчасти")
def create_part(
    part_data: PartModel,
    create_part_service: CreateParts = Depends(get_create_parts_service),
):
    try:
        create_part_service.create(part_data)
        return {"message": "Запчасть успешно создана"}
    except PartsAlreadyExists:
        raise HTTPException(status_code=400, detail="Такая запчасть уже есть")


@parts_router.get("/", summary="Метод для получения списка всех запчастей")
def get_all_parts(
    get_all_parts_service: GetAllParts = Depends(get_all_parts_service),
):
    return get_all_parts_service.get_all()


@parts_router.patch("/{part_id}", summary="Метод для обновления запчасти")
def update_part(
    part_id: int,
    part_data: PartModel,
    update_part_service: UpdateParts = Depends(get_update_parts_service),
):
    try:
        update_part_service.update(part_id, part_data)
        return {"message": f"Запчасть с ID {part_id} успешно обновлена"}
    except PartsNotFoundException:
        raise HTTPException(
            status_code=404, detail=f"Запчасть с ID {part_id} не найдена"
        )


@parts_router.delete("/{part_id}", summary="Метод для удаления запчасти")
def delete_part(
    part_id: int,
    delete_part_service: DeleteParts = Depends(get_delete_parts_service),
):
    try:
        delete_part_service.delete(part_id)
        return {"message": f"Запчасть с ID {part_id} успешно удалена"}
    except PartsNotFoundException:
        raise HTTPException(
            status_code=404, detail=f"Запчасть с ID {part_id} не найдена"
        )
