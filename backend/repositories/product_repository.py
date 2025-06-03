import pymysql
from models.product import Product
from database.db import get_db_connection
from typing import List

class ProductRepository:
    def create(self, product: Product) -> int:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = """
                    INSERT INTO products (name, description, price, stock)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (product.name, product.description, product.price, product.stock))
                conn.commit()
                return cursor.lastrowid

    def get_by_id(self, product_id: int) -> Product | None:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = "SELECT * FROM products WHERE id = %s"
                cursor.execute(query, (product_id,))
                result = cursor.fetchone()
                return Product(**result) if result else None

    def get_all(self) -> List[Product]:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM products")
                results = cursor.fetchall()
                return [Product(**result) for result in results]

    def update(self, product_id: int, product: Product) -> bool:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = """
                    UPDATE products 
                    SET name = %s, description = %s, price = %s, stock = %s
                    WHERE id = %s
                """
                cursor.execute(query, (product.name, product.description, product.price, product.stock, product_id))
                conn.commit()
                return cursor.rowcount > 0

    def delete(self, product_id: int) -> bool:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = "DELETE FROM products WHERE id = %s"
                cursor.execute(query, (product_id,))
                conn.commit()
                return cursor.rowcount > 0