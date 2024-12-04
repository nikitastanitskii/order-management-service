class PartNameCannotBeEmpty(Exception):
    """Название запчасти пустое."""

    pass


class PartsAlreadyExists(Exception):
    """Запчасть с таким именем уже существует"""

    pass


class PartsNotFoundException(Exception):
    """Запчасть не найдена"""

    pass
