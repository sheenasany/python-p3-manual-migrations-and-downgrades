"""Renaming students to scholars

Revision ID: 3d806f4b4991
Revises: 791279dd0760
Create Date: 2023-03-02 13:31:05.530285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d806f4b4991'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
