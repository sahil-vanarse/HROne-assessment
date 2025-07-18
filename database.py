from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://sahilvanarse13:sahilvanarse13@ecommerce-hrone.aot51wi.mongodb.net/?retryWrites=true&w=majority&appName=ecommerce-HROne")
client = AsyncIOMotorClient(MONGO_URL)
db = client["ecommerce-HROne"]
products_collection = db["products"]
orders_collection = db["orders"]
