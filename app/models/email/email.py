"""
Email model for tracking sent emails.
"""
from typing import Optional, Dict
from uuid import UUID, uuid4

from sqlalchemy import Boolean, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.enums import EmailStatus
from app.core.types import StrictString, JSONType
from app.models.base import Base
from app.models.email.mixins import EmailTrackingMixin
from app.schemas.email import EmailSender, EmailRecipient, EmailTemplateVariables


class Email(EmailTrackingMixin, Base):
    """Email model."""
    
    __tablename__ = "emails"
    __table_args__ = (
        {"sqlite_on_conflict": "ROLLBACK"}
    )

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
        StrictString(255),
        nullable=False,
    )
    to_email: Mapped[str] = mapped_column(
        StrictString(255),
        nullable=False,
        index=True,
    )
    subject: Mapped[str] = mapped_column(
        StrictString(255),
        nullable=False,
    )
    body_html: Mapped[str] = mapped_column(
        StrictString,
        nullable=False,
    )
    body_text: Mapped[Optional[str]] = mapped_column(
        StrictString,
        nullable=True,
    )
    variables: Mapped[Optional[Dict]] = mapped_column(
        JSONType(schema=EmailTemplateVariables),
        nullable=True,
    )
    sender_info: Mapped[Optional[Dict]] = mapped_column(
        JSONType(schema=EmailSender),
        nullable=True,
    )
    recipient_info: Mapped[Optional[Dict]] = mapped_column(
        JSONType(schema=EmailRecipient),
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