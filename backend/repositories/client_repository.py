import pymysql
from models.client import Client
from database.db import get_db_connection
from typing import List

class ClientRepository:
    def create(self, client: Client) -> int:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = """
                    INSERT INTO clients (nombres, apellidos, correo)
                    VALUES (%s, %s, %s)
                """
                cursor.execute(query, (client.nombres, client.apellidos, client.correo))
                conn.commit()
                return cursor.lastrowid

    def get_by_id(self, client_id: int) -> Client | None:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = "SELECT * FROM clients WHERE id = %s"
                cursor.execute(query, (client_id,))
                result = cursor.fetchone()
                return Client(**result) if result else None

    def get_all(self) -> List[Client]:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM clients")
                results = cursor.fetchall()
                return [Client(**result) for result in results]

    def update(self, client_id: int, client: Client) -> bool:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = """
                    UPDATE clients 
                    SET nombres = %s, apellidos = %s, correo = %s
                    WHERE id = %s
                """
                cursor.execute(query, (client.nombres, client.apellidos, client.correo, client_id))
                conn.commit()
                return cursor.rowcount > 0

    def delete(self, client_id: int) -> bool:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = "DELETE FROM clients WHERE id = %s"
                cursor.execute(query, (client_id,))
                conn.commit()
                return cursor.rowcount > 0