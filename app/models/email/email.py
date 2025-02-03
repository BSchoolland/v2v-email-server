"""
Email model for tracking sent emails.
"""
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy import String, Text, Boolean, ForeignKey, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum

from app.models.base import Base


class EmailStatus(str, enum.Enum):
    """Email status enumeration."""
    QUEUED = "queued"
    SENDING = "sending"
    SENT = "sent"
    DELIVERED = "delivered"
    FAILED = "failed"
    BOUNCED = "bounced"
    SPAM = "spam"
    BLOCKED = "blocked"


class Email(Base):
    """Email model."""
    
    __tablename__ = "emails"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )
    client_id: Mapped[UUID] = mapped_column(
        ForeignKey("clients.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    template_id: Mapped[Optional[UUID]] = mapped_column(
        ForeignKey("email_templates.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    status: Mapped[EmailStatus] = mapped_column(
        Enum(EmailStatus),
        default=EmailStatus.QUEUED,
        nullable=False,
        index=True,
    )
    from_email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    to_email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )
    subject: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    body_html: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    body_text: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )
    variables: Mapped[Optional[str]] = mapped_column(
        Text,  # JSON string of variables used
        nullable=True,
    )
    sent_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    delivered_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    opened_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    clicked_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    error_message: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )
    retry_count: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )
    is_test: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    # Relationships
    client = relationship("Client", back_populates="emails")
    template = relationship("EmailTemplate", back_populates="emails")
    bounces = relationship("Bounce", back_populates="email")

    def __repr__(self) -> str:
        """String representation."""
        return f"<Email {self.id}: {self.status.value}>" 