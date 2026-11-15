BASE_URL = "http://localhost:8088/api"


def test_browse_pages_match_single_request(make_actor, outings):
    host = make_actor()
    for _ in range(10):
        host.outings.create()

    first_ten = outings.browse(limit=10)
    page1 = outings.browse(limit=5)
    page2 = outings.browse(limit=5, after=page1.next_cursor)

    ids_all = [item.id for item in first_ten.items]
    ids_page1 = [item.id for item in page1.items]
    ids_page2 = [item.id for item in page2.items]

    assert ids_page1 + ids_page2 == ids_all


def test_browse_with_wrong_cursor(outings):
    outings.browse(limit=5, after="abc", expected=400)
