"""revision24

Revision ID: d8ad1d0c73e9
Revises: 66267d015fd7
Create Date: 2023-06-10 03:01:47.484057

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd8ad1d0c73e9'
down_revision = '66267d015fd7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('token_live_time', sa.DateTime(), nullable=True))
    op.drop_column('user', 'time_create_token')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('time_create_token', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.drop_column('user', 'token_live_time')
    # ### end Alembic commands ###
