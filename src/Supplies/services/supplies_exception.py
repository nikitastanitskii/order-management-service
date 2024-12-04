class SuppliesNameCannotBeEmpty(Exception):
    """Название поставки пустое."""

    pass


class SuppliesAlreadyExists(Exception):
    """Поставка с таким именем уже существует"""

    pass


class SuppliesNotFoundException(Exception):
    """Поставка не найдена"""

    pass
