from alembic import op

revision = '0002_add_indexes'
down_revision = '0001_add_additional_info'
branch_labels = None
depends_on = None

def upgrade():
    op.create_index('idx_tournear_country', 'tournear', ['country'])
    op.create_index('idx_tournear_qualification', 'tournear', ['qualification_level'])
    op.create_index('idx_player_rating', 'player', ['rating'])

def downgrade():
    op.drop_index('idx_tournear_country', table_name='tournear')
    op.drop_index('idx_tournear_qualification', table_name='tournear')
    op.drop_index('idx_player_rating', table_name='player')

