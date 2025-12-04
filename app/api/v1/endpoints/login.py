from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db
from app.core.security import create_access_token, verify_password
from app.crud.user import get_user_by_email
from app.schemas.token import Token

router = APIRouter()


@router.post("/access-token", response_model=Token)
async def login_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: AsyncSession = Depends(get_db)
):
    """
    Login OAuth2 compatível com Swagger (recebe username e password).
    """
    # 1. Busca o usuário pelo email (username do form)
    user = await get_user_by_email(db, email=form_data.username)

    # 2. Verifica se usuário existe e se a senha bate
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Email ou senha incorretos")

    # 3. Gera o token
    return {
        "access_token": create_access_token(user.email),
        "token_type": "bearer",
    }