"""
Pydantic schemas for email-related data.
"""
from typing import Dict, List, Optional, Union

from pydantic import BaseModel, EmailStr, HttpUrl


class EmailVariables(BaseModel):
    """Schema for email template variables."""
    
    required: List[str]
    defaults: Dict[str, Union[str, int, float, bool]]
    descriptions: Dict[str, str]


class EmailTemplateVariables(BaseModel):
    """Schema for rendered email template variables."""
    
    values: Dict[str, Union[str, int, float, bool]]
    metadata: Optional[Dict[str, str]] = None


class EmailRecipient(BaseModel):
    """Schema for email recipient data."""
    
    email: EmailStr
    name: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None


class EmailSender(BaseModel):
    """Schema for email sender data."""
    
    email: EmailStr
    name: Optional[str] = None
    reply_to: Optional[EmailStr] = None


class EmailLinks(BaseModel):
    """Schema for tracking links in emails."""
    
    original: HttpUrl
    tracking: HttpUrl
    click_count: int = 0
    last_clicked: Optional[str] = None 