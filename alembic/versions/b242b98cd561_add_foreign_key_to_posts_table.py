"""add foreign key to posts table

Revision ID: b242b98cd561
Revises: 36278f66baa5
Create Date: 2022-08-03 18:38:22.404121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b242b98cd561'
down_revision = '36278f66baa5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable = False))
    op.create_foreign_key('posts_users_fk', source_table= 'posts', referent_table= 'users',
    local_cols=['owner_id'], remote_cols= ['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk',table_name= 'posts')
    op.drop_column('posts', 'column_id')
    pass
