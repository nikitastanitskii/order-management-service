from fastapi import Depends
from src.Suppliers.repository.suppliers_repository import (
    BaseSuppliersRepository,
    get_suppliers_repository,
)
from src.Suppliers.schemas.suppliers_schemas import SuppliersModel
from src.Suppliers.services.suppliers_exception import SuppliersNameCannotBeEmpty


class UpdateSuppliers:
    def __init__(self, supplier_repository: BaseSuppliersRepository) -> None:
        self.__repository = supplier_repository

    def update(self, supplier_id: int, supplier_data: SuppliersModel) -> None:
        """Функция для обновления данных о поставщике"""
        if not supplier_data.name:
            raise SuppliersNameCannotBeEmpty(
                "Название поставщика не может быть пустым."
            )
        self.__repository.update(supplier_id, supplier_data)


def get_update_supplier_service(
    supplier_repository: BaseSuppliersRepository = Depends(get_suppliers_repository),
) -> UpdateSuppliers:
    return UpdateSuppliers(supplier_repository=supplier_repository)
