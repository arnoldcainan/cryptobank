from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db,get_current_user
from app.schemas.wallet import WalletCreate, WalletResponse
from app.crud import wallet as crud_wallet
from app.services import market_data
from app.models.user import User

router = APIRouter()


@router.post("/", response_model=WalletResponse, status_code=201)
async def create_wallet(
        wallet_in: WalletCreate,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)  # <--- Exige Token
):
    """
    Cria carteira para o USUÁRIO LOGADO.
    """
    # Usamos o ID do token (current_user.id), não o da URL
    return await crud_wallet.create_wallet(db=db, wallet=wallet_in, user_id=current_user.id)


@router.get("/summary")
async def get_wallet_summary(
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)  # <--- Exige Token
):
    """
    Retorna resumo do USUÁRIO LOGADO.
    """
    wallets = await crud_wallet.get_wallets_by_user(db, current_user.id)

    btc_price = await market_data.get_crypto_price("bitcoin", "usd")

    summary = []
    for w in wallets:
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
