"""empty message

Revision ID: 939c82573218
Revises: 
Create Date: 2023-09-13 15:16:45.066264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '939c82573218'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('staff',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('record_name', sa.String(length=64), nullable=True),
    sa.Column('artist_name', sa.String(length=64), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('staff_associated_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['staff_associated_id'], ['staff.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('records')
    op.drop_table('staff')
    # ### end Alembic commands ###
