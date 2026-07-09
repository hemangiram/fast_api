# FastAPI CRUD API

A simple **FastAPI** project demonstrating CRUD (Create, Read, Update, Delete) operations for managing products using **SQLAlchemy** and **SQLite**.

---

## 🚀 Features

- FastAPI REST API
- SQLAlchemy ORM
- SQLite Database
- Product CRUD Operations
  - Create Product
  - Get All Products
  - Get Product by ID
  - Update Product
  - Delete Product
- Pydantic Validation
- Interactive Swagger API Documentation

---

## 🛠️ Technologies Used

- Python 3.x
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- SQLite

---

## 📂 Project Structure

fast_api/
│
├── project/
│   ├── static/
│   ├── templates/
│   └── __pycache__/        # Ignored
│
├── .gitignore
├── README.md
├── main.py
├── database.py
├── database_models.py
├── crud.py
├── schema.py
├── requirements.txt
├── products.db
│
├── .venv/                  # Ignored
└── __pycache__/            # Ignored

---

## 📥 Clone the Repository

Using HTTPS (Recommended)

```bash
git clone https://github.com/your_username/your_repository.git
cd fast_api
```

Or using SSH

```bash
git clone git@github.com:your_username/your_repository.git
cd fast_api
```

---

## 🐍 Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 📦 Install Dependencies

If you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 📚 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📌 Available API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /products | Get all products |
| GET | /products/{id} | Get product by ID |
| POST | /products | Create a new product |
| PUT | /products/{id} | Update a product |
| DELETE | /products/{id} | Delete a product |

---

## ▶️ Example Request

Create Product

```json
{
    "name": "Laptop",
    "price": 50000,
    "description": "Gaming Laptop"
}
```

---

## 📄 License

This project is created for learning FastAPI and SQLAlchemy.

---

## 👨‍💻 Author

Your Name

GitHub: https://github.com/your_username