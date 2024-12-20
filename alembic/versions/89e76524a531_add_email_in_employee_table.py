"""add email in employee table

Revision ID: 89e76524a531
Revises: 1419743a01b4
Create Date: 2024-11-12 18:23:49.425310

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '89e76524a531'
down_revision: Union[str, None] = '1419743a01b4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employees', sa.Column('email', sa.String(length=100), nullable=True))
    op.create_index(op.f('ix_employees_email'), 'employees', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_employees_email'), table_name='employees')
    op.drop_column('employees', 'email')
    # ### end Alembic commands ###
