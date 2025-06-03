from pydantic import BaseModel, EmailStr

class Client(BaseModel):
    id: int | None = None
    nombres: str
    apellidos: str
    correo: EmailStr