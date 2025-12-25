from alembic import op
import sqlalchemy as sa

revision = '0001_add_additional_info'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('tournear', sa.Column('additional_info', sa.JSON(), nullable=True))

def downgrade():
    op.drop_column('tournear', 'additional_info')

