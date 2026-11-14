import hashlib
import os
import secrets

import psycopg

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgres://postgres:dev@localhost:5432/muster?sslmode=disable",
)


def hash_token(raw: str) -> str:
    return hashlib.sha256(raw.encode()).hexdigest()


def mint_verification_token(
    hiker_id: str, purpose: str = "email_verification", ttl_hours: int = 24
) -> str:
    raw = secrets.token_hex(32)
    with psycopg.connect(DATABASE_URL) as conn:
        conn.execute(
            """
            INSERT INTO auth_tokens (id, hiker_id, token_hash, purpose, created_at, expires_at)
            VALUES (gen_random_uuid(), %s, %s, %s, now(), now() + make_interval(hours => %s))
            """,
            (hiker_id, hash_token(raw), purpose, ttl_hours),
        )
    return raw
