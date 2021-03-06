"""empty message

Revision ID: 624fdb72d185
Revises: 6741511e9b44
Create Date: 2022-03-17 20:01:51.060678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '624fdb72d185'
down_revision = '6741511e9b44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('phone', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
