import uvicorn
from fastapi import APIRouter, FastAPI
from src.Parts.views import parts_router
from src.Suppliers.views import suppliers_router
from src.Supplies.views import supplies_router
from src.migrations.initial_migration import (
    create_parts_table,
    create_suppliers_table,
    create_supplies_table,
)


def lifespan(function):
    create_parts_table()
    create_suppliers_table()
    create_supplies_table()

    yield


app = FastAPI(lifespan=lifespan)

api_router = APIRouter()
api_router.include_router(parts_router, tags=["PARTS"])
api_router.include_router(suppliers_router, tags=["SUPPLIERS"])
api_router.include_router(supplies_router, tags=["SUPPLIES"])
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(app)
