from fastapi import APIRouter, Depends, HTTPException
from src.Suppliers.schemas.Suppliers_schemas import SuppliersModel
from src.Suppliers.services.create_suppliers import (
    CreateSuppliers,
    get_create_supplier_service,
)
from src.Suppliers.services.delete_suppliers import (
    DeleteSuppliers,
    get_delete_supplier_service,
)
from src.Suppliers.services.get_all_suppliers import (
    GetAllSuppliers,
    get_all_suppliers_service,
)
from src.Suppliers.services.suppliers_exception import (
    SuppliersAlreadyExists,
    SuppliersNotFoundException,
)
from src.Suppliers.services.update_suppliers import (
    UpdateSuppliers,
    get_update_supplier_service,
)

suppliers_router = APIRouter(prefix="/suppliers")


@suppliers_router.post("/", summary="Метод для создания поставщика")
def create_supplier(
    supplier_data: SuppliersModel,  # Принятие данных нового поставщика
    create_supplier_service: CreateSuppliers = Depends(get_create_supplier_service),
):
    try:
        create_supplier_service.create(
            supplier_data
        )  # Вызов метода сервиса для создания поставщика
        return {"message": "Поставщик успешно создан"}
    except SuppliersAlreadyExists:
        raise HTTPException(status_code=404, detail="Такой поставщик уже существует")


@suppliers_router.get("/", summary="Метод для получения списка всех поставщиков")
def get_all_suppliers(
    get_suppliers_service: GetAllSuppliers = Depends(get_all_suppliers_service),
):
    suppliers = (
        get_suppliers_service.get_all()
    )  # Вызов метода сервиса для получения всех поставщиков
    return suppliers


@suppliers_router.patch("/{supplier_id}", summary="Метод для обновления поставщика")
def update_supplier(
    supplier_id: int,
    supplier_data: SuppliersModel,  # Принятие новых данных поставщика
    update_supplier_service: UpdateSuppliers = Depends(get_update_supplier_service),
):
    try:
        update_supplier_service.update(
            supplier_id, supplier_data
        )  # Вызов метода сервиса для обновления данных поставщика
        return {"message": f"Данные поставщика с ID {supplier_id} успешно обновлены"}
    except SuppliersNotFoundException:
        raise HTTPException(
            status_code=404, detail=f"Поставщик с ID {supplier_id} не найден"
        )


@suppliers_router.delete("/{supplier_id}", summary="Метод для удаления поставщика")
def delete_supplier(
    supplier_id: int,
    delete_supplier_service: DeleteSuppliers = Depends(get_delete_supplier_service),
):
    try:
        delete_supplier_service.delete(
            supplier_id
        )  # Вызов метода сервиса для удаления поставщика
        return {"message": f"Поставщик с ID {supplier_id} успешно удален"}
    except SuppliersNotFoundException:
        raise HTTPException(
            status_code=404, detail=f"Поставщик с ID {supplier_id} не найден"
        )
