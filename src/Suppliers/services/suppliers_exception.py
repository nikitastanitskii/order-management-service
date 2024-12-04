class SuppliersNameCannotBeEmpty(Exception):
    """Название поставщика пустое."""

    pass


class SuppliersAlreadyExists(Exception):
    """Поставщик с таким именем уже существует"""

    pass


class SuppliersNotFoundException(Exception):
    """Поставщик не найден"""

    pass
