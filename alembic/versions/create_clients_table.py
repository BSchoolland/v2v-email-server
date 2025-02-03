"""create clients table

Revision ID: create_clients_table
Revises: 
Create Date: 2024-01-20 10:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from app.models.base import UUID

# revision identifiers, used by Alembic.
revision: str = 'create_clients_table'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create clients table."""
    op.create_table(
        'clients',
        sa.Column('id', UUID(), primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('api_key', sa.String(64), nullable=False),
        sa.Column('website_url', sa.String(255), nullable=False),
        sa.Column('contact_email', sa.String(255), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default='1'),
        sa.Column('rate_limit', sa.Integer(), nullable=False, server_default='60'),
        sa.Column('description', sa.String(500), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    )

    op.create_index(
        'ix_clients_api_key',
        'clients',
        ['api_key'],
        unique=True
    )


def downgrade() -> None:
    """Drop clients table."""
    op.drop_index('ix_clients_api_key')
    op.drop_table('clients') 