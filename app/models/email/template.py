"""
Email template model.
"""
from typing import Optional, Dict
from uuid import UUID, uuid4

from sqlalchemy import Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.types import StrictString, JSONType
from app.models.base import Base
from app.models.email.mixins import EmailTrackingMixin
from app.schemas.email import EmailVariables


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
        StrictString(100),
        nullable=False,
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
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )
    description: Mapped[Optional[str]] = mapped_column(
        StrictString(500),
        nullable=True,
    )
    variables: Mapped[Optional[Dict]] = mapped_column(
        JSONType(schema=EmailVariables),
        nullable=True,
    )

    # Relationships
    client = relationship("Client", back_populates="templates")
    emails = relationship("Email", back_populates="template")

    def __repr__(self) -> str:
        """String representation."""
        return f"<EmailTemplate {self.name}>" 