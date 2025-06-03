from fastapi import FastAPI, Depends
from models.product import Product
from models.client import Client
from services.product_service import ProductService, get_product_service
from services.client_service import ClientService, get_client_service
from database.db import init_db
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permite solicitudes desde este origen
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)
# Initialize database before starting the application
init_db()

# Product API Routes
@app.post("/products/", response_model=Product)
async def create_product(product: Product, service: ProductService = Depends(get_product_service)):
    product_id = service.create_product(product)
    return await get_product(product_id, service)

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int, service: ProductService = Depends(get_product_service)):
    return service.get_product(product_id)

@app.get("/products/", response_model=List[Product])
async def get_all_products(service: ProductService = Depends(get_product_service)):
    return service.get_all_products()

@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, product: Product, service: ProductService = Depends(get_product_service)):
    return service.update_product(product_id, product)

@app.delete("/products/{product_id}")
async def delete_product(product_id: int, service: ProductService = Depends(get_product_service)):
    service.delete_product(product_id)
    return {"message": "Product deleted successfully"}

# Client API Routes
@app.post("/clients/", response_model=Client)
async def create_client(client: Client, service: ClientService = Depends(get_client_service)):
    client_id = service.create_client(client)
    return await get_client(client_id, service)

@app.get("/clients/{client_id}", response_model=Client)
async def get_client(client_id: int, service: ClientService = Depends(get_client_service)):
    return service.get_client(client_id)

@app.get("/clients/", response_model=List[Client])
async def get_all_clients(service: ClientService = Depends(get_client_service)):
    return service.get_all_clients()

@app.put("/clients/{client_id}", response_model=Client)
async def update_client(client_id: int, client: Client, service: ClientService = Depends(get_client_service)):
    return service.update_client(client_id, client)

@app.delete("/clients/{client_id}")
async def delete_client(client_id: int, service: ClientService = Depends(get_client_service)):
    service.delete_client(client_id)
    return {"message": "Client deleted successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)