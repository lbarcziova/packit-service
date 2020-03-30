"""added project name and git fields

Revision ID: 61d0f32eda4b
Revises: 70dcb6140e11
Create Date: 2020-03-10 19:11:36.729552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "61d0f32eda4b"
down_revision = "70dcb6140e11"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("git_projects", sa.Column("https_url", sa.String(), nullable=True))
    op.add_column("copr_builds", sa.Column("project_name", sa.String(), nullable=True))
    op.add_column("copr_builds", sa.Column("owner", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("copr_builds", "owner")
    op.drop_column("copr_builds", "project_name")
    op.drop_column("git_projects", "https_url")
    # ### end Alembic commands ###