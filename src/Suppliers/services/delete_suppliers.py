from fastapi import Depends
from src.Suppliers.repository.suppliers_repository import (
    BaseSuppliersRepository,
    get_suppliers_repository,
)
from src.Suppliers.services.suppliers_exception import SuppliersNotFoundException


class DeleteSuppliers:
    def __init__(self, supplier_repository: BaseSuppliersRepository) -> None:
        self.__repository = supplier_repository

    def delete(self, supplier_id: int) -> None:
        # Проверяем, существует ли запчасть
        if self.__repository.get(supplier_id):
            self.__repository.delete(supplier_id)
        else:
            raise SuppliersNotFoundException(f"Запчасть с ID {supplier_id} не найдена.")


def get_delete_supplier_service(
    supplier_repository: BaseSuppliersRepository = Depends(get_suppliers_repository),
) -> DeleteSuppliers:
    return DeleteSuppliers(supplier_repository=supplier_repository)
