"""
Client model for API authentication.
"""
from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Client(Base):
    """API client model."""
    
    __tablename__ = "clients"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    api_key: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        nullable=False,
        index=True,
    )
    website_url: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    contact_email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )
    rate_limit: Mapped[int] = mapped_column(
        default=60,  # Default to 60 requests per minute
        nullable=False,
    )
    description: Mapped[Optional[str]] = mapped_column(
        String(500),
        nullable=True,
    )

    def __repr__(self) -> str:
        """String representation."""
        return f"<Client {self.name}>" 