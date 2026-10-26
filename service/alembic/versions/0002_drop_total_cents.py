from alembic import op
import sqlalchemy as sa

revision = '0002'
down_revision = '0001'


def upgrade():
    op.drop_column('orders', 'total_cents')


def downgrade():
    pass
