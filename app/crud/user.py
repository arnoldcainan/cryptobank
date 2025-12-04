from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.schemas.user import UserCreate
from passlib.context import CryptContext

# Configuração de Hashing de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_user_by_email(db: AsyncSession, email: str):
    # Query assíncrona moderna (select)
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()


async def create_user(db: AsyncSession, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)

    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name
    )

    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)  # Recarrega o ID gerado pelo banco
    return db_user