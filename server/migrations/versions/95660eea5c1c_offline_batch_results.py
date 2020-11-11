# pylint: disable=invalid-name
"""Offline batch results

Revision ID: 95660eea5c1c
Revises: 8bc5c2037187
Create Date: 2020-11-11 20:01:56.196066+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "95660eea5c1c"
down_revision = "8bc5c2037187"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "offline_batch_result",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("jurisdiction_id", sa.String(length=200), nullable=False),
        sa.Column("batch_name", sa.String(length=200), nullable=False),
        sa.Column("contest_choice_id", sa.String(length=200), nullable=False),
        sa.Column("result", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["contest_choice_id"],
            ["contest_choice.id"],
            name=op.f("offline_batch_result_contest_choice_id_fkey"),
            ondelete="cascade",
        ),
        sa.ForeignKeyConstraint(
            ["jurisdiction_id"],
            ["jurisdiction.id"],
            name=op.f("offline_batch_result_jurisdiction_id_fkey"),
            ondelete="cascade",
        ),
        sa.PrimaryKeyConstraint(
            "jurisdiction_id",
            "batch_name",
            "contest_choice_id",
            name=op.f("offline_batch_result_pkey"),
        ),
    )
    op.add_column(
        "jurisdiction",
        sa.Column("finalized_offline_batch_results_at", sa.DateTime(), nullable=True),
    )


def downgrade():  # pragma: no cover
    pass
    # # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_column("jurisdiction", "finalized_offline_batch_results_at")
    # op.drop_table("offline_batch_result")
    # ### end Alembic commands ###
