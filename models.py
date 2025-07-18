# models.py
from database import products_collection, orders_collection
from pymongo import ASCENDING

async def create_product(product):
    product_dict = product.dict()
    result = await products_collection.insert_one(product_dict)
    return {"id": str(result.inserted_id)}  # changed to id

async def list_products(name=None, size=None, limit=10, offset=0):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes.size"] = size

    cursor = products_collection.find(query).sort("_id", ASCENDING).skip(offset).limit(limit)
    products = []
    async for doc in cursor:
        products.append({
            "id": str(doc["_id"]),  # return as "id"
            "name": doc["name"],
            "price": doc["price"]
        })
    return {
        "data": products,
        "page": {
            "next": offset + limit,
            "limit": len(products),
            "previous": offset - limit
        }
    }

async def create_order(order):
    order_dict = order.dict()
    result = await orders_collection.insert_one(order_dict)
    return {"id": str(result.inserted_id)}  # changed to id

async def list_orders(user_id, limit=10, offset=0):
    from bson import ObjectId
    from database import products_collection

    query = {"userId": user_id}
    cursor = orders_collection.find(query).sort("_id", ASCENDING).skip(offset).limit(limit)

    orders = []
    async for order in cursor:
        total = 0
        items = []
        for item in order["items"]:
            product_id = item["productId"]
            qty = item["qty"]

            product = await products_collection.find_one({"_id": ObjectId(product_id)})
            if not product:
                continue  # skip missing products

            price = product.get("price", 0)
            total += price * qty

            items.append({
                "productDetails": {
                    "id": str(product["_id"]),
                    "name": product["name"]
                },
                "qty": qty
            })

        orders.append({
            "id": str(order["_id"]),
            "items": items,
            "total": round(total, 2)
        })

    return {
        "data": orders,
        "page": {
            "next": offset + limit,
            "limit": len(orders),
            "previous": offset - limit
        }
    }

