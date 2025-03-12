from uuid import UUID

from sqlalchemy.sql import text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class ShortURL(Base):
    id: Mapped[UUID] = mapped_column(
        comment="Primary model key",
        server_default=text("gen_random_uuid()"),
        nullable=False,
        primary_key=True,
        index=True,
        unique=True,
    )
    original_url: Mapped[str] = mapped_column(
        comment="Original url",
        nullable=False,
    )
    short_url: Mapped[str] = mapped_column(
        comment="Original url",
        nullable=False,
    )
