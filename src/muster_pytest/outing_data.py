import random
from datetime import UTC, datetime, timedelta

from muster_pytest.identity import tag

HOURS = [48, 72, 96, 120]

OUTINGS = [
    {
        "title": "Poo Poo Point",
        "destination": "Issaquah",
        "meet_label": "South Bellevue P&R",
        "max_size": 10,
        "host_seats": 3,
        "cost_per_seat_cents": 350,
        "difficulty": "moderate",
        "pace": "relaxed",
        "notes": "Paraglider launch views at the top",
    },
    {
        "title": "Rattlesnake Ledge",
        "destination": "North Bend",
        "meet_label": "Eastgate P&R",
        "max_size": 8,
        "host_seats": 4,
        "cost_per_seat_cents": 2550,
        "difficulty": "easy",
        "pace": "relaxed",
        "notes": "Busy trail, early start",
    },
    {
        "title": "Mount Si",
        "destination": "North Bend",
        "meet_label": "Issaquah Highlands P&R",
        "max_size": 6,
        "host_seats": 3,
        "cost_per_seat_cents": 450,
        "difficulty": "hard",
        "pace": "moderate",
        "notes": "Bring plenty of water, 3100 ft gain",
    },
]


def hours_from_now_iso(hours: int) -> str:
    return (datetime.now(UTC) + timedelta(hours=hours)).isoformat()


def unique_outing(**overrides) -> dict:
    o = random.choice(OUTINGS)
    t = tag()
    return {
        **o,
        "title": f"{o['title']} {t}",
        "starts_at": hours_from_now_iso(random.choice(HOURS)),
        **overrides,
    }
