"""empty message

Revision ID: e0bee2ce3531
Revises: daa01433a5bc
Create Date: 2019-03-12 21:53:48.104143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0bee2ce3531'
down_revision = 'daa01433a5bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('cash', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'cash')
    # ### end Alembic commands ###
