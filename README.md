# e14-agents

Test fixture of the E14.4 live acceptance of the PI platform. No real data, no secrets.

- `service/` — the orders HTTP service; its contract is `service/openapi.yaml`, migrations in `service/alembic/` and `service/sql/`.
- `web/` — a client of the orders API.

Changes go through pull requests: `main` requires one approval.
