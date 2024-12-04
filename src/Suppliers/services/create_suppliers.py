from fastapi import Depends
from src.Suppliers.repository.suppliers_repository import (
    BaseSuppliersRepository,
    get_suppliers_repository,
)
from src.Suppliers.schemas.Suppliers_schemas import SuppliersModel
from src.Suppliers.services.suppliers_exception import SuppliersNameCannotBeEmpty


class CreateSuppliers:
    def __init__(self, supplier_repository: BaseSuppliersRepository) -> None:
        self.__repository = supplier_repository

    def create(self, supplier_data: SuppliersModel) -> None:
        if not supplier_data.name:
            raise SuppliersNameCannotBeEmpty(
                "Название поставщика не может быть пустым."
            )
        self.__repository.create(supplier_data)


def get_create_supplier_service(
    supplier_repository: BaseSuppliersRepository = Depends(get_suppliers_repository),
) -> CreateSuppliers:
    return CreateSuppliers(supplier_repository=supplier_repository)
