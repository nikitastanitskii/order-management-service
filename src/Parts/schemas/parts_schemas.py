from pydantic import BaseModel
from decimal import Decimal


class PartModel(BaseModel):
    name: str
    description: str
    price: Decimal
    in_stock: int
