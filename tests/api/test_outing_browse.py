BASE_URL = "http://localhost:8088/api"


def test_browse_returns_outings(outings):
    data = outings.browse(limit=10)

    assert isinstance(data["items"], list)
    assert len(data["items"]) == 10
    assert all(item["status"] == "open" for item in data["items"])


def test_browse_pagination_has_no_overlap(outings):
    page1 = outings.browse(limit=5)
    cursor = page1["next_cursor"]

    page2 = outings.browse(limit=5, after=cursor)
    ids1 = {item["id"] for item in page1["items"]}
    ids2 = {item["id"] for item in page2["items"]}
    assert len(ids1) + len(ids2) == 10
    assert len(ids1) == 5 == len(ids2)
    assert ids1 & ids2 == set()
