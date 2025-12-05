from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import session, engine
import database_models
from schemas import ProductSchema
from typing import List

app = FastAPI()

# Create DB tables
database_models.Base.metadata.create_all(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

# Sample products to initialize DB
products = [
    {"id":1, "name":"phone", "description":"a smartphone", "price":99, "quantity":4},
    {"id":2, "name":"laptop", "description":"a personal pc", "price":999, "quantity":3},
    {"id":3, "name":"table", "description":"a wooden table", "price":99.6, "quantity":5},
]

def init_db():
    db = session()
    count = db.query(database_models.Product).count()
    if count == 0:
        for prod in products:
            db.add(database_models.Product(**prod))
        db.commit()

init_db()

@app.get("/")
def greet():
    return "welcome to fastapi"

# Get all products
@app.get("/products/get", response_model=List[ProductSchema])
def get_products(db: Session = Depends(get_db)):
    return db.query(database_models.Product).all()

# Get product by ID
@app.get("/product/id_by", response_model=ProductSchema)
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Add product
@app.post("/post_product/add", response_model=ProductSchema)
def post_product(product: ProductSchema, db: Session = Depends(get_db)):
    db_product = database_models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Update product
@app.patch("/products/update", response_model=ProductSchema)
def update_product(id: int, updated_fields: ProductSchema, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    db_product.name = updated_fields.name
    db_product.description = updated_fields.description
    db_product.price = updated_fields.price
    db_product.quantity = updated_fields.quantity

    db.commit()
    db.refresh(db_product)
    return db_product

# Delete product
@app.delete("/product/delete")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(db_product)
    db.commit()
    return {"detail": "product deleted"}
