def test_host_can_create_outing(make_actor):
    host = make_actor()
    outing = host.outings.create(max_size=4)
    assert host.hiker["id"] == outing.host_id
    assert outing.max_size == 4
    assert outing.status == "open"
