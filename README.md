Crystal clear now bro. You want **one single `README.md` file** — no chat, no separation, no breaks — just one file you can **click "Copy" once** and paste into your `README.md`.

Here is that **complete, 1-shot README.md**. No fragments. No back and forth.

---

### ✅ Copy everything below from the line after this into your `README.md`:

```markdown
# 🛒 HROne E-commerce Backend API

This is a backend service for managing products and orders using FastAPI and MongoDB Atlas. Built for the HROne Internship Assignment.

---

## 🚀 Features

- ✅ Add products with sizes and prices  
- ✅ Filter and paginate product listings  
- ✅ Place orders for multiple products  
- ✅ Retrieve user orders with joined product details  
- ✅ Paginated order history with total amount  

---

## 🧱 Tech Stack

- **FastAPI** (Python framework)  
- **MongoDB Atlas (M0 Free Tier)**  
- **Render** for deployment (Free Plan)  

---

## 📁 Folder Structure

```

HROne/
├── main.py               # App entry point
├── database.py           # MongoDB connection
├── models.py             # DB logic for products & orders
├── schemas.py            # Pydantic models (validation)
├── routes/
│   ├── products.py       # Routes for /products
│   └── orders.py         # Routes for /orders
├── .env                  # Mongo URI (not pushed to GitHub)
└── README.md             # This file

```

---

## ⚙️ How to Run Locally

1. **Clone the repository**
```

git clone [https://github.com/sahil-vanarse/HROne-assessment]((https://github.com/sahil-vanarse/HROne-assessment))
cd hrone-backend

```

2. **Create virtual environment**
```

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

```

3. **Install dependencies**
```

pip install -r requirements.txt

```

4. **Create a `.env` file**
```

MONGO\_URL=mongodb+srv://<username>:<password>@cluster.mongodb.net/?retryWrites=true\&w=majority

```

5. **Run the app**
```

uvicorn main\:app --reload

```

6. Open in browser:
```

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

````

---

## 🌍 Deploy to Render (Free Plan)

1. Push code to GitHub (public repo)
2. Go to https://render.com and create a **New Web Service**
3. Connect your GitHub repo
4. Use the following settings:
- **Runtime:** Python
- **Start Command:**
  ```
  uvicorn main:app --host 0.0.0.0 --port 10000
  ```
- **Environment Variable:**
  ```
  MONGO_URL = your-mongodb-uri
  ```
5. Deploy and wait for live URL like:  
````

[https://hrone-assessment.onrender.com/]((https://hrone-assessment.onrender.com/))

````

This URL is what you submit in the form.

---

## 🧪 API Examples

### 📦 POST `/products`

**Request:**
```json
{
"name": "Basic T-Shirt",
"price": 499.99,
"sizes": [
 { "size": "M", "quantity": 10 },
 { "size": "L", "quantity": 5 }
]
}
````

**Response:**

```json
{ "id": "product_id_here" }
```

---

### 📦 GET `/products?name=shirt&size=M&limit=10&offset=0`

**Response:**

```json
{
  "data": [
    {
      "id": "product_id",
      "name": "Basic T-Shirt",
      "price": 499.99
    }
  ],
  "page": {
    "next": 10,
    "limit": 1,
    "previous": -10
  }
}
```

---

### 🛒 POST `/orders`

**Request:**

```json
{
  "userId": "user_123",
  "items": [
    { "productId": "product_id", "qty": 2 }
  ]
}
```

**Response:**

```json
{ "id": "order_id" }
```

---

### 📄 GET `/orders/user_123`

**Response:**

```json
{
  "data": [
    {
      "id": "order_id",
      "items": [
        {
          "productDetails": {
            "id": "product_id",
            "name": "Basic T-Shirt"
          },
          "qty": 2
        }
      ],
      "total": 999.98
    }
  ],
  "page": {
    "next": 10,
    "limit": 1,
    "previous": -10
  }
}
```

---

## 🧪 Example .env File

```
MONGO_URL=mongodb+srv://username:password@yourcluster.mongodb.net/?retryWrites=true&w=majority
```

---


---

## 👤 Author

**Sahil Vanarse** – July 2025
GitHub: [https://github.com/sahil-vanarse](https://github.com/sahil-vanarse)

```

---

✅ Done. That’s **one complete file**, formatted perfectly.

Let me know once you paste it and push it — I’ll help deploy to Render if needed.
```
