from alembic import op
import sqlalchemy as sa

revision = '0004'
down_revision = '0003'


def upgrade():
    op.drop_column('orders', 'id')


def downgrade():
    pass
