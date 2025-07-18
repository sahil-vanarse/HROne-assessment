# schemas.py
from pydantic import BaseModel
from typing import List, Dict

class SizeItem(BaseModel):
    size: str
    quantity: int

class ProductCreate(BaseModel):
    name: str
    price: float
    sizes: List[SizeItem]

class ProductResponse(BaseModel):
    id: str


class PaginatedProducts(BaseModel):
    data: List[ProductResponse]
    page: Dict[str, int]

class OrderItem(BaseModel):
    productId: str
    qty: int

class OrderCreate(BaseModel):
    userId: str
    items: List[OrderItem]

class OrderResponse(BaseModel):
    id: str


class ProductDetails(BaseModel):
    id: str
    name: str

class EnrichedOrderItem(BaseModel):
    productDetails: ProductDetails
    qty: int

class EnrichedOrder(BaseModel):
    id: str
    items: List[EnrichedOrderItem]
    total: float

class PaginatedOrders(BaseModel):
    data: List[EnrichedOrder]
    page: Dict[str, int]
