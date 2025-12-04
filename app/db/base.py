from datetime import datetime
from typing import Any
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import func


class Base(DeclarativeBase):
    id: Any

    # Gera o nome da tabela automaticamente baseado no nome da classe (ex: UserModel -> user_model)
    # Mas vamos simplificar para usar o nome em minúsculo
    @property
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    # Colunas padrão para auditoria (Recrutadores amam isso)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())