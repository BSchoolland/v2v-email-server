"""
Mail server functionality.
"""
import asyncio
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate, make_msgid

from app.core.config import settings

logger = logging.getLogger(__name__)


class MailServer:
    """Mail server for handling SMTP communication."""

    def __init__(self):
        """Initialize the mail server."""
        self.hostname = settings.MAIL_SERVER_HOSTNAME
        self.port = settings.MAIL_SERVER_TLS_PORT if settings.MAIL_SERVER_USE_TLS else settings.MAIL_SERVER_PORT
        self.use_tls = settings.MAIL_SERVER_USE_TLS
        self.from_name = settings.EMAILS_FROM_NAME
        self.from_domain = settings.EMAILS_FROM_DOMAIN
        self.from_email = settings.EMAILS_FROM_EMAIL

    async def create_message(
        self,
        to_email: str,
        subject: str,
        content: str,
        content_type: str = "plain",
    ) -> MIMEMultipart:
        """Create an email message with proper headers."""
        message = MIMEMultipart()
        message["From"] = f"{self.from_name} <{self.from_email}>"
        message["To"] = to_email
        message["Subject"] = subject
        message["Date"] = formatdate(localtime=True)
        message["Message-ID"] = make_msgid(domain=self.from_domain)
        
        # Add body
        message.attach(MIMEText(content, content_type))
        
        return message

    async def send_mail(
        self,
        to_email: str,
        subject: str,
        content: str,
        content_type: str = "plain",
    ) -> bool:
        """Send an email using direct SMTP."""
        message = await self.create_message(to_email, subject, content, content_type)
        
        try:
            # Create a connection to our local Postfix server
            reader, writer = await asyncio.open_connection(
                self.hostname,
                self.port,
            )
            
            # Read the server greeting
            response = await reader.read(1024)
            if not response.startswith(b"220"):
                raise Exception(f"Bad server greeting: {response}")
            
            # EHLO/HELO
            writer.write(f"EHLO {self.hostname}\r\n".encode())
            await writer.drain()
            response = await reader.read(1024)
            if not response.startswith(b"250"):
                raise Exception(f"EHLO failed: {response}")
            
            # MAIL FROM
            writer.write(f"MAIL FROM:<{self.from_email}>\r\n".encode())
            await writer.drain()
            response = await reader.read(1024)
            if not response.startswith(b"250"):
                raise Exception(f"MAIL FROM failed: {response}")
            
            # RCPT TO
            writer.write(f"RCPT TO:<{to_email}>\r\n".encode())
            await writer.drain()
            response = await reader.read(1024)
            if not response.startswith(b"250"):
                raise Exception(f"RCPT TO failed: {response}")
            
            # DATA
            writer.write(b"DATA\r\n")
            await writer.drain()
            response = await reader.read(1024)
            if not response.startswith(b"354"):
                raise Exception(f"DATA failed: {response}")
            
            # Send message
            writer.write(message.as_string().encode() + b"\r\n.\r\n")
            await writer.drain()
            response = await reader.read(1024)
            if not response.startswith(b"250"):
                raise Exception(f"Message send failed: {response}")
            
            # QUIT
            writer.write(b"QUIT\r\n")
            await writer.drain()
            
            writer.close()
            await writer.wait_closed()
            
            logger.info(f"Email sent successfully to {to_email}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send email to {to_email}: {str(e)}")
            raise


# Create a global mail server instance
mail_server = MailServer() 