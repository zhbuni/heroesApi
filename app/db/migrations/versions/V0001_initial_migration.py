"""initial

Revision ID: 5ab173dba505
Revises: 
Create Date: 2024-03-26 15:24:45.927354

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '5ab173dba505'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('heroes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('counter_heroes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hero_id', sa.Integer(), nullable=True),
    sa.Column('counter_hero_id', sa.Integer(), nullable=True),
    sa.Column('winrate', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['counter_hero_id'], ['heroes.id'], ),
    sa.ForeignKeyConstraint(['hero_id'], ['heroes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role_presences',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('winrate', sa.Double(), nullable=False),
    sa.Column('presence', sa.Double(), nullable=False),
    sa.Column('hero_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['hero_id'], ['heroes.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('role_presences')
    op.drop_table('counter_heroes')
    op.drop_table('roles')
    op.drop_table('heroes')
    # ### end Alembic commands ###
