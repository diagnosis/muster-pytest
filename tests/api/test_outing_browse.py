import json

import httpx

BASE_URL = "http://localhost:8088/api"


def test_browse_returns_outings():
    resp = httpx.get(f"{BASE_URL}/outings", params={"limit": 10})
    assert resp.status_code == 200
    body = resp.json()
    items = body["data"]["items"]
    assert isinstance(items, list)
    assert len(items) == 10
    assert all(item["status"] == "open" for item in items)


def test_browse_pagination_has_no_overlap():
    page1 = httpx.get(f"{BASE_URL}/outings", params={"limit": 5}).json()
    cursor = page1["data"]["next_cursor"]

    page2 = httpx.get(
        f"{BASE_URL}/outings", params={"limit": 5, "after": cursor}
    ).json()
    ids1 = {item["id"] for item in page1["data"]["items"]}
    ids2 = {item["id"] for item in page2["data"]["items"]}
    assert len(ids1) + len(ids2) == 10
    assert len(ids1) == 5 == len(ids2)
    assert ids1 & ids2 == set()
