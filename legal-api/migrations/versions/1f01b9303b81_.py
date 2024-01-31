"""empty message

Revision ID: 1f01b9303b81
Revises: e85053684b3c
Create Date: 2020-02-12 10:30:06.267601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f01b9303b81'
down_revision = 'e85053684b3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('filing_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_comments_filing_id'), 'comments', ['filing_id'], unique=False)
    op.create_foreign_key(None, 'comments', 'filings', ['filing_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_index(op.f('ix_comments_filing_id'), table_name='comments')
    op.drop_column('comments', 'filing_id')
    # ### end Alembic commands ###