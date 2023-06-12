"""revision6

Revision ID: 63c429b078b0
Revises: d85cdbe45fd3
Create Date: 2023-06-04 00:21:39.379803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63c429b078b0'
down_revision = 'd85cdbe45fd3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('hashed_token', sa.String(length=1024), nullable=False))
    op.add_column('user', sa.Column('live_time_token', sa.String(length=1024), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'live_time_token')
    op.drop_column('user', 'hashed_token')
    # ### end Alembic commands ###
