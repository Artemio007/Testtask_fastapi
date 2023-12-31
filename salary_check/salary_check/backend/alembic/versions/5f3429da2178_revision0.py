"""revision0

Revision ID: 5f3429da2178
Revises: 
Create Date: 2023-05-31 00:32:01.261941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f3429da2178'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('salarydata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=30), nullable=False),
    sa.Column('user_middle_name', sa.String(length=30), nullable=False),
    sa.Column('user_last_name', sa.String(length=30), nullable=False),
    sa.Column('time_get_data', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_salarydata_id'), 'salarydata', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_salarydata_id'), table_name='salarydata')
    op.drop_table('salarydata')
    # ### end Alembic commands ###
