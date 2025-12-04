from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.wallet import Wallet
from app.schemas.wallet import WalletCreate

async def create_wallet(db: AsyncSession, wallet: WalletCreate, user_id: int):
    db_wallet = Wallet(
        name=wallet.name,
        balance=wallet.balance,
        user_id=user_id
    )
    db.add(db_wallet)
    await db.commit()
    await db.refresh(db_wallet)
    return db_wallet

async def get_wallets_by_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(Wallet).where(Wallet.user_id == user_id))
    return result.scalars().all()