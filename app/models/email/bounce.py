"""
Bounce model for tracking email bounces.
"""
from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy import String, Text, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.enums import BounceType
from app.models.base import Base


class Bounce(Base):
    """Bounce model."""
    
    __tablename__ = "bounces"
    __table_args__ = (
        {"sqlite_on_conflict": "ROLLBACK"}
    )

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )
    email_id: Mapped[UUID] = mapped_column(
        ForeignKey("emails.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    bounce_type: Mapped[BounceType] = mapped_column(
        Enum(BounceType),
        default=BounceType.UNKNOWN,
        nullable=False,
        index=True,
    )
    status_code: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
    )
    diagnostic_code: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
    )
    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    raw_response: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    # Relationships
    email = relationship("Email", back_populates="bounces")

    def __repr__(self) -> str:
        """String representation."""
        return f"<Bounce {self.id}: {self.bounce_type.value}>" 