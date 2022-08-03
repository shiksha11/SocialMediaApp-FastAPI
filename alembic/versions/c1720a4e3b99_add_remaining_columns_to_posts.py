"""add remaining columns to posts

Revision ID: c1720a4e3b99
Revises: b242b98cd561
Create Date: 2022-08-03 18:47:30.940929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1720a4e3b99'
down_revision = 'b242b98cd561'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable = 'FALSE', server_default = sa.text('NOW()')),)
    op.add_column('posts', sa.Column('published', sa.Boolean, nullable = False, server_default = 'TRUE'),)

def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
