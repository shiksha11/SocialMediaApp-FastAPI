"""add content column to posts

Revision ID: dc8fd457bc6e
Revises: a271810e15d9
Create Date: 2022-08-03 12:07:22.739847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc8fd457bc6e'
down_revision = 'a271810e15d9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable = False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
