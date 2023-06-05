"""object_meet model

Revision ID: a4ca9a326162
Revises: f4f271e49bb1
Create Date: 2023-06-05 12:33:34.866784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4ca9a326162'
down_revision = 'f4f271e49bb1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('object_meet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('x', sa.Integer(), nullable=False),
    sa.Column('y', sa.Integer(), nullable=False),
    sa.Column('z_index', sa.Integer(), nullable=False),
    sa.Column('orientation', sa.String(), nullable=False),
    sa.Column('meet_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['meet_id'], ['meets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_object_meet_id'), 'object_meet', ['id'], unique=False)
    op.create_index(op.f('ix_object_meet_name'), 'object_meet', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_object_meet_name'), table_name='object_meet')
    op.drop_index(op.f('ix_object_meet_id'), table_name='object_meet')
    op.drop_table('object_meet')
    # ### end Alembic commands ###
