from alembic import op

revision = '0003_add_gin_index'
down_revision = '0002_add_indexes'
branch_labels = None
depends_on = None

def upgrade():
    op.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm;')
    
    op.create_index('idx_tournear_additional_info', 'tournear', ['additional_info'], postgresql_using='gin')
    
    op.create_index('idx_tournear_name_search', 'tournear', ['t_name'], postgresql_using='gin', postgresql_ops={'t_name': 'gin_trgm_ops'})

def downgrade():
    op.drop_index('idx_tournear_additional_info', table_name='tournear')
    op.drop_index('idx_tournear_name_search', table_name='tournear')

