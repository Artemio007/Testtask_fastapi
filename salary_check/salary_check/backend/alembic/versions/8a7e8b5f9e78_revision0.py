"""revision0

Revision ID: 8a7e8b5f9e78
Revises: 5f3429da2178
Create Date: 2023-05-31 22:27:01.331004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a7e8b5f9e78'
down_revision = '5f3429da2178'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('salarydata', sa.Column('salary_size', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('salarydata', 'salary_size')
    # ### end Alembic commands ###