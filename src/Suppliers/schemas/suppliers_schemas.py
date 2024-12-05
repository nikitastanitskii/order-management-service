from pydantic import BaseModel


class SuppliersModel(BaseModel):
    id: int
    name: str
    contact: str
