"""
Email template model.
"""
from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy import String, Text, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.email.mixins import EmailTrackingMixin


class EmailTemplate(EmailTrackingMixin, Base):
    """Email template model."""
    
    __tablename__ = "email_templates"
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
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
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
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )
    description: Mapped[Optional[str]] = mapped_column(
        String(500),
        nullable=True,
    )
    variables: Mapped[Optional[str]] = mapped_column(
        Text,  # JSON string of required variables
        nullable=True,
    )

    # Relationships
    client = relationship("Client", back_populates="templates")
    emails = relationship("Email", back_populates="template")

    def __repr__(self) -> str:
        """String representation."""
        return f"<EmailTemplate {self.name}>" 