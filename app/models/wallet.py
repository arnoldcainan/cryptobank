from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Float
from app.db.base import Base


class Wallet(Base):
    __tablename__ = "wallets"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)  # Ex: "Investimento Longo Prazo"
    balance: Mapped[float] = mapped_column(Float, default=0.0)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner = relationship("User", back_populates="wallets")