"""revision12

Revision ID: b421060d7e2b
Revises: 1045c92beede
Create Date: 2023-06-06 23:04:10.174119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b421060d7e2b'
down_revision = '1045c92beede'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_salary_id_fkey', 'user', type_='foreignkey')
    op.drop_column('user', 'salary_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('salary_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('user_salary_id_fkey', 'user', 'salarydata', ['salary_id'], ['id'])
    # ### end Alembic commands ###