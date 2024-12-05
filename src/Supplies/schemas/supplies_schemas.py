from datetime import datetime
from pydantic import BaseModel


class SuppliesModel(BaseModel):
    part_id: int
    supplier_id: int
    quantity: int
    date: datetime
