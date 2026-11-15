def test_join_outing_success(make_actor):
    host = make_actor()
    hiker = make_actor()
    outing = host.outings.create(max_size=6, host_seats=4)
    outing_id = outing.id
    join_request = hiker.join_requests.request_join(outing_id, guests=2)
    host.join_requests.accept(join_request.id)
    detail = host.outings.details(outing_id)
    assert detail.people_count == 4
    assert len(detail.roster) == 1
    assert detail.waiting_count == 0
