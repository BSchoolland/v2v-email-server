"""
Email endpoints.
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session
from app.core.mail import mail_server
from app.models.auth.client import Client
from app.core.security import get_client_by_api_key

router = APIRouter()


@router.post("/send")
async def send_email(
    to_email: str,
    subject: str,
    content: str,
    client: Annotated[Client, Depends(get_client_by_api_key)],
) -> dict:
    """Send an email."""
    try:
        await mail_server.send_mail(
            to_email=to_email,
            subject=subject,
            content=content,
        )
        return {"status": "success", "message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to send email: {str(e)}",
        ) 