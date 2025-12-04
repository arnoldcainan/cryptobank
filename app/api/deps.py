from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import AsyncSessionLocal
from app.core.config import settings
from app.core.security import ALGORITHM, SECRET_KEY
from app.crud.user import get_user_by_email
from app.models.user import User
from app.schemas.token import TokenPayload

# O tokenUrl diz ao Swagger onde ele deve ir para fazer login (o botão do cadeado)
reusable_oauth2 = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/login/access-token")


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


# Essa é a função que protege as rotas
async def get_current_user(
        db: AsyncSession = Depends(get_db),
        token: str = Depends(reusable_oauth2)
) -> User:
    try:
        # Tenta decodificar o Token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except (JWTError, ValueError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Não foi possível validar as credenciais",
        )

    # Busca o usuário no banco
    user = await get_user_by_email(db, email=str(token_data.sub))
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return user