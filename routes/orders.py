from fastapi import APIRouter
from schemas import OrderCreate, OrderResponse, PaginatedOrders
from models import create_order, list_orders

router = APIRouter()

@router.post("/orders", status_code=201, response_model=OrderResponse)
async def add_order(order: OrderCreate):
    return await create_order(order)

@router.get("/orders/{user_id}", response_model=PaginatedOrders)
async def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    return await list_orders(user_id, limit, offset)
