from fastapi import APIRouter, FastAPI, HTTPException, Depends
from src.Suppliers.services.suppliers_exception import SuppliersNotFoundException
from src.Supplies.schemas.Supplies_schemas import SuppliesModel
from src.Supplies.services.create_supplies import (
    CreateSupplies,
    get_create_supply_service,
)
from src.Supplies.services.delete_supplies import (
    DeleteSupplies,
    get_delete_supply_service,
)
from src.Supplies.services.get_all_supplies import (
    GetAllSupplies,
    get_all_supplies_service,
)
from src.Supplies.services.supplies_exception import (
    SuppliesAlreadyExists,
    SuppliesNotFoundException,
)
from src.Supplies.services.update_supplies import (
    UpdateSupplies,
    get_update_supply_service,
)

supplies_router = APIRouter(prefix="/supplies")


@supplies_router.post("/", summary="Метод для создания поставки")
def create_supplies(
    supplies_data: SuppliesModel,
    create_supplies_service: CreateSupplies = Depends(get_create_supply_service),
):
    try:
        create_supplies_service.create(supplies_data)
        return {"message": "Поставка успешно создана"}
    except SuppliesAlreadyExists:
        raise HTTPException(status_code=400, detail="Такая поставка уже существует")


@supplies_router.get("/", summary="Метод для получения списка всех поставок")
def get_all_supplies(
    get_supplies_service: GetAllSupplies = Depends(get_all_supplies_service),
):
    supplies = get_supplies_service.get_all()
    return supplies


@supplies_router.patch("/{supply_id}", summary="Метод для обновления поставки")
def update_supply(
    supplies_id: int,
    supplies_data: SuppliesModel,
    update_supplies_service: UpdateSupplies = Depends(get_update_supply_service),
):
    try:
        update_supplies_service.update(supplies_id, supplies_data)
        return {"message": f"Поставка с ID {supplies_id} успешно обновлена"}
    except SuppliersNotFoundException:
        raise HTTPException(
            status_code=404, detail=f"Поставка с ID {supplies_id} не найдена"
        )


@supplies_router.delete("/{supply_id}", summary="Метод для удаления поставки")
def delete_supply(
    supplies_id: int,
    delete_supplies_service: DeleteSupplies = Depends(get_delete_supply_service),
):
    try:
        delete_supplies_service.delete(supplies_id)
        return {"message": f"Поставка с ID {supplies_id} успешно удалена"}
    except SuppliesNotFoundException:
        raise HTTPException(
            status_code=404, detail=f"Поставка с ID {supplies_id} не найдена"
        )
