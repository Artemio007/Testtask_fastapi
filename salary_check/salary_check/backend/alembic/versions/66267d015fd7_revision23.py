"""revision23

Revision ID: 66267d015fd7
Revises: 85ee76fc18e0
Create Date: 2023-06-10 00:34:43.772741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66267d015fd7'
down_revision = '85ee76fc18e0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'salarydata', ['user_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'salarydata', type_='unique')
    # ### end Alembic commands ###
