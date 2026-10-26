"""Alembic environment of the fixture: offline only, no database URL is configured here."""
from alembic import context

context.configure(url=None, target_metadata=None, literal_binds=True)
with context.begin_transaction():
    context.run_migrations()
