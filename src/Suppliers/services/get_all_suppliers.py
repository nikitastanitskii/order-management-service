from fastapi import Depends
from src.Suppliers.repository.suppliers_repository import (
    BaseSuppliersRepository,
    get_suppliers_repository,
)
from src.Suppliers.schemas.Suppliers_schemas import SuppliersModel


class GetAllSuppliers:
    def __init__(self, supplier_repository: BaseSuppliersRepository) -> None:
        self.__repository = supplier_repository

    def get_all(self) -> list[SuppliersModel]:
        return self.__repository.get_all()


def get_all_suppliers_service(
    supplier_repository: BaseSuppliersRepository = Depends(get_suppliers_repository),
) -> GetAllSuppliers:
    return GetAllSuppliers(supplier_repository=supplier_repository)
