"""empty message

Revision ID: a5303ba477ab
Revises: 21aa8d3e5bc1
Create Date: 2022-03-16 09:58:07.767731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5303ba477ab'
down_revision = '21aa8d3e5bc1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transports', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_created', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transports', schema=None) as batch_op:
        batch_op.drop_column('date_created')

    # ### end Alembic commands ###