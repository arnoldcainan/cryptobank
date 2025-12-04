from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserResponse
from app.crud import user as crud_user
from app.api.deps import get_db

router = APIRouter()


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    Cria um novo usuário no Cryptobank.
    """
    # 1. Verifica se email já existe
    user_exists = await crud_user.get_user_by_email(db, email=user_in.email)
    if user_exists:
        raise HTTPException(
            status_code=400,
            detail="Este e-mail já está cadastrado."
        )

    # 2. Cria o usuário
    new_user = await crud_user.create_user(db, user=user_in)
    return new_user