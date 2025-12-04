from fastapi import APIRouter
from app.api.v1.endpoints import users, wallets

api_router = APIRouter()

# Agrupa as rotas de usuário sob o prefixo /users
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(wallets.router, prefix="/wallets", tags=["Wallets"])