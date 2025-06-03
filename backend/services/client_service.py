from fastapi import HTTPException
from models.client import Client
from repositories.client_repository import ClientRepository
from typing import List

class ClientService:
    def __init__(self, repository: ClientRepository):
        self.repository = repository

    def create_client(self, client: Client) -> int:
        if not client.nombres or not client.apellidos:
            raise HTTPException(status_code=400, detail="Names and surnames cannot be empty")
        return self.repository.create(client)

    def get_client(self, client_id: int) -> Client:
        client = self.repository.get_by_id(client_id)
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        return client

    def get_all_clients(self) -> List[Client]:
        return self.repository.get_all()

    def update_client(self, client_id: int, client: Client) -> Client:
        if not client.nombres or not client.apellidos:
            raise HTTPException(status_code=400, detail="Names and surnames cannot be empty")
        success = self.repository.update(client_id, client)
        if not success:
            raise HTTPException(status_code=404, detail="Client not found")
        return self.get_client(client_id)

    def delete_client(self, client_id: int) -> None:
        success = self.repository.delete(client_id)
        if not success:
            raise HTTPException(status_code=404, detail="Client not found")

def get_client_service() -> ClientService:
    return ClientService(ClientRepository())