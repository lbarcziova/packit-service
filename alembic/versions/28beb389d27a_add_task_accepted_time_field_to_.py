"""Add task_accepted_time field to CoprBuildModel

Revision ID: 28beb389d27a
Revises: 800abbbb23c9
Create Date: 2021-08-03 12:46:06.704728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "28beb389d27a"
down_revision = "800abbbb23c9"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "copr_builds", sa.Column("task_accepted_time", sa.DateTime(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("copr_builds", "task_accepted_time")
    # ### end Alembic commands ###