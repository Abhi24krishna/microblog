"""followers

Revision ID: 0482c1b97187
Revises: 5cf53cf13e8f
Create Date: 2021-06-22 22:49:03.379321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0482c1b97187'
down_revision = '5cf53cf13e8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
