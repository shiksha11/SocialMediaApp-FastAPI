"""add user table

Revision ID: 36278f66baa5
Revises: dc8fd457bc6e
Create Date: 2022-08-03 12:09:44.440377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36278f66baa5'
down_revision = 'dc8fd457bc6e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable = False),
                    sa.Column('email', sa.String(), nullable = False),
                    sa.Column('password', sa.String(), nullable = False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone = True), 
                                server_default = sa.text('now()'), nullable = False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
