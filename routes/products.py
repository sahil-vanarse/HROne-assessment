# products.py
from fastapi import APIRouter, Query
from typing import Optional
from schemas import ProductCreate, ProductResponse, PaginatedProducts
from models import create_product, list_products

router = APIRouter()

@router.post("/products", status_code=201, response_model=ProductResponse)
async def add_product(product: ProductCreate):
    return await create_product(product)

@router.get("/products", response_model=PaginatedProducts)
async def get_products(
    name: Optional[str] = Query(None),
    size: Optional[str] = Query(None),
    limit: int = 10,
    offset: int = 0,
):
    return await list_products(name, size, limit, offset)
