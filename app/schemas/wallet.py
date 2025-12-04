from pydantic import BaseModel, ConfigDict


class WalletBase(BaseModel):
    name: str
    balance: float = 0.0


class WalletCreate(WalletBase):
    pass


class WalletResponse(WalletBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)