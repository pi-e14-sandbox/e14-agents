from alembic import op
import sqlalchemy as sa

revision = '0003'
down_revision = '0001'


def upgrade():
    op.drop_column('orders', 'customer_id')


def downgrade():
    pass
