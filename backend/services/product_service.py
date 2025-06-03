from fastapi import HTTPException
from models.product import Product
from repositories.product_repository import ProductRepository
from typing import List

class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def create_product(self, product: Product) -> int:
        if product.price < 0:
            raise HTTPException(status_code=400, detail="Price cannot be negative")
        if product.stock < 0:
            raise HTTPException(status_code=400, detail="Stock cannot be negative")
        return self.repository.create(product)

    def get_product(self, product_id: int) -> Product:
        product = self.repository.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

    def get_all_products(self) -> List[Product]:
        return self.repository.get_all()

    def update_product(self, product_id: int, product: Product) -> Product:
        if product.price < 0:
            raise HTTPException(status_code=400, detail="Price cannot be negative")
        if product.stock < 0:
            raise HTTPException(status_code=400, detail="Stock cannot be negative")
        success = self.repository.update(product_id, product)
        if not success:
            raise HTTPException(status_code=404, detail="Product not found")
        return self.get_product(product_id)

    def delete_product(self, product_id: int) -> None:
        success = self.repository.delete(product_id)
        if not success:
            raise HTTPException(status_code=404, detail="Product not found")

def get_product_service() -> ProductService:
    return ProductService(ProductRepository())