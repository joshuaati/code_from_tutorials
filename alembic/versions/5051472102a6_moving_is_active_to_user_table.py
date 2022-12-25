"""Moving is_active to user table

Revision ID: 5051472102a6
Revises: 21e3f83c6140
Create Date: 2022-12-25 22:29:40.811630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5051472102a6'
down_revision = '21e3f83c6140'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profiles', 'is_active')
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_active')
    op.add_column('profiles', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
