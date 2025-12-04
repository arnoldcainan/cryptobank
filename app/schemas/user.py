from pydantic import BaseModel, EmailStr, ConfigDict


# Base comum (para evitar repetição)
class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None


# O que precisamos para CRIAR um usuário (tem senha)
class UserCreate(UserBase):
    password: str


# O que retornamos para o cliente (SEM senha)
class UserResponse(UserBase):
    id: int
    is_active: bool

    # Configuração nova do Pydantic V2 para ler do ORM
    model_config = ConfigDict(from_attributes=True)