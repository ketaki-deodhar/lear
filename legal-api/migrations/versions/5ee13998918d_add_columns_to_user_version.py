"""add_columns_to_user_version

Revision ID: 5ee13998918d
Revises: b9f84f7a7c44
Create Date: 2022-11-25 16:08:05.078690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ee13998918d'
down_revision = 'b9f84f7a7c44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users_version', sa.Column('idp_userid', sa.String(length=256)))
    op.add_column('users_version', sa.Column('login_source', sa.String(length=200)))


def downgrade():
    op.drop_column('users_version', 'login_source')
    op.drop_column('users_version', 'idp_userid')
