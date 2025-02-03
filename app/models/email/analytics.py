"""
Analytics model for tracking email statistics.
"""
from datetime import date
from uuid import UUID

from sqlalchemy import Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.types import StrictString
from app.models.base import Base


class EmailAnalytics(Base):
    """Email analytics model for daily statistics."""
    
    __tablename__ = "email_analytics"
    __table_args__ = (
        {"sqlite_on_conflict": "ROLLBACK"},
        {"unique_together": ("client_id", "date", "template_name")},
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    client_id: Mapped[UUID] = mapped_column(
        ForeignKey("clients.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        index=True,
    )
    sent_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )
    delivered_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )
    opened_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )
    clicked_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )
    bounced_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )
    spam_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )
    template_name: Mapped[str] = mapped_column(
        StrictString(100),
        nullable=False,
        index=True,
    )

    # Relationships
    client = relationship("Client", back_populates="analytics")

    def __repr__(self) -> str:
        """String representation."""
        return f"<EmailAnalytics {self.date}: {self.sent_count} sent>" 