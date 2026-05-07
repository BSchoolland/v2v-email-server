"""
Application configuration module.
"""
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""
    
    # API Configuration
    PROJECT_NAME: str = "V2V Email Server"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str = "development_secret_key"  # Change in production
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]  # Configure in production
    
    # Mail Server Settings
    MAIL_SERVER_HOSTNAME: str = "mail.yourdomain.com"
    MAIL_SERVER_PORT: int = 25  # Standard SMTP port
    MAIL_SERVER_USE_TLS: bool = True
    MAIL_SERVER_TLS_PORT: int = 587  # TLS port
    DKIM_PRIVATE_KEY_PATH: str = "/etc/opendkim/keys/mail.private"
    DKIM_SELECTOR: str = "mail"  # DKIM selector for key rotation
    
    # Email Settings
    EMAILS_FROM_NAME: str = "V2V Email Server"
    EMAILS_FROM_DOMAIN: str = "yourdomain.com"
    EMAILS_FROM_EMAIL: str = "noreply@yourdomain.com"
    
    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 60
    RATE_LIMIT_PER_DOMAIN: int = 100  # Limit emails per domain per minute
    
    # Logging
    LOG_LEVEL: str = "INFO"
    MAIL_LOG_PATH: str = "/var/log/v2v-email/mail.log"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.SQLALCHEMY_DATABASE_URI = (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"
        )


settings = Settings() 