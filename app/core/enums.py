"""
Core enumerations used across the application.
"""
import enum


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


class BounceType(str, enum.Enum):
    """Bounce type enumeration."""
    HARD = "hard"  # Permanent failure
    SOFT = "soft"  # Temporary failure
    BLOCK = "block"  # Blocked by recipient
    SPAM = "spam"  # Marked as spam
    TECHNICAL = "technical"  # Technical failure
    UNKNOWN = "unknown"  # Unknown reason 