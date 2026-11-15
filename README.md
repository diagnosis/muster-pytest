# muster-pytest

API test suite for [Muster](https://muster.safadev.app), written in Python with pytest, httpx and Pydantic.

## Run

    uv sync
    uv run pytest tests/api -v

Requires the Muster API running locally on port 8088 and a local Postgres (see `DATABASE_URL` in `src/muster_pytest/db.py`).