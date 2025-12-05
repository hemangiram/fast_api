# fast_api

A simple FastAPI project with CRUD operations for managing products.

## Features

- FastAPI framework for building REST APIs
- SQLAlchemy ORM for database interactions
- SQLite as the default database
- CRUD operations for Product model:
  - Create a product
  - Read all products / by ID
  - Update product details
  - Delete a product
- Pydantic schemas for request validation and response models

## Project Structure

1. Clone the repository:

```bash
git clone git@github.com:your_username/your_repositoryname.git
cd fast_api

python -m venv .venv
source .venv/bin/activate  # Linux/macOS

pip install fastapi uvicorn sqlalchemy pydantic

uvicorn main:app --reload
