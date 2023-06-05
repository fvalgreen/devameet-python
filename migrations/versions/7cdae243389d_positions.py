"""positions

Revision ID: 7cdae243389d
Revises: ac83fbdf9d8c
Create Date: 2023-06-05 14:33:22.024648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cdae243389d'
down_revision = 'ac83fbdf9d8c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('position', sa.Column('avatar', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('position', 'avatar')
    # ### end Alembic commands ###
