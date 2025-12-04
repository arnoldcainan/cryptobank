from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db
from app.schemas.wallet import WalletCreate, WalletResponse
from app.crud import wallet as crud_wallet
from app.services import market_data  # <--- Importamos nosso serviço

router = APIRouter()


@router.post("/{user_id}/", response_model=WalletResponse, status_code=201)
async def create_wallet(
        user_id: int,
        wallet_in: WalletCreate,
        db: AsyncSession = Depends(get_db)
):
    """
    Cria uma nova carteira para um usuário específico.
    """
    return await crud_wallet.create_wallet(db=db, wallet=wallet_in, user_id=user_id)


@router.get("/{user_id}/summary")
async def get_wallet_summary(user_id: int, db: AsyncSession = Depends(get_db)):
    """
    Retorna as carteiras e quanto elas valem em BTC hoje.
    """
    wallets = await crud_wallet.get_wallets_by_user(db, user_id)

    # Busca o preço do Bitcoin em tempo real (Async!)
    btc_price = await market_data.get_crypto_price("bitcoin", "usd")

    summary = []
    for w in wallets:
        # Evita divisão por zero
        btc_value = (w.balance / btc_price) if btc_price > 0 else 0
        summary.append({
            "wallet_name": w.name,
            "balance_usd": w.balance,
            "estimated_btc": round(btc_value, 6)
        })

    return {
        "btc_price_now": btc_price,
        "wallets": summary
    }
