from alembic import op
import sqlalchemy as sa

revision = '0001'
down_revision = None


def upgrade():
    op.create_table('orders', sa.Column('id', sa.Integer(), primary_key=True), sa.Column('customer_id', sa.String(64), nullable=False), sa.Column('total_cents', sa.Integer(), nullable=False, server_default='0'))


def downgrade():
    op.drop_table('orders')
