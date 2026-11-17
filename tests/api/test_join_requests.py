import pytest

from muster_pytest.envelope import ApiError


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
    hiker_detail = hiker.outings.details(outing_id)
    assert hiker_detail.my_request.status == "accepted"

def test_hiker_requests(make_actor):
    host = make_actor()
    hiker =  make_actor()
    outing = host.outings.create(max_size=6, host_seats=4)
    hiker.join_requests.request_join(outing.id, guests=1)
    host_detail = host.outings.details(outing.id)
    assert host_detail.waiting_count == 1

def test_host_declines(make_actor):
    host = make_actor()
    hiker = make_actor()
    outing = host.outings.create(max_size=6, host_seats=5)
    join_request = hiker.join_requests.request_join(outing.id)
    host.join_requests.decline(join_request.id)
    hiker_detail = hiker.outings.details(outing.id)
    assert hiker_detail.my_request.status == "declined"

def test_hiker_withdraws(make_actor):
    host = make_actor()
    hiker = make_actor()
    outing = host.outings.create(max_size=6, host_seats=5)
    join_request = hiker.join_requests.request_join(outing.id)
    hiker.join_requests.withdraw(outing.id)
    host_detail = host.outings.details(outing.id)
    hiker_detail = hiker.outings.details(outing.id)
    assert len(host_detail.withdrawn) == 1
    assert hiker_detail.my_request.status == "withdrawn"

def test_member_accepts(make_actor):
    host = make_actor()
    hiker = make_actor()
    member = make_actor()
    outing = host.outings.create(max_size=6, host_seats=5)
    host.join_requests.accept(member.join_requests.request_join(outing.id).id)
    with pytest.raises(ApiError) as e:
        member.join_requests.accept(hiker.join_requests.request_join(outing.id).id)
    assert e.value.status == 403
    assert e.value.code == "forbidden"

def test_requests_twice(make_actor):
    host = make_actor()
    hiker = make_actor()
    outing = host.outings.create(max_size=6, host_seats=5)
    hiker.join_requests.request_join(outing.id)
    with pytest.raises(ApiError) as e:
        hiker.join_requests.request_join(outing.id)
    assert e.value.status == 409
    assert e.value.code == "conflict"

def test_host_requests_their_own_outing(make_actor):
    host = make_actor()
    outing = host.outings.create(max_size=6, host_seats=5)
    with pytest.raises(ApiError) as e:
        host.join_requests.request_join(outing.id)

    assert e.value.status == 400
    assert e.value.code == "bad_request"

def test_anon_requests(make_actor,join_request):
    host = make_actor()
    outing = host.outings.create(max_size=6, host_seats=5)
    with pytest.raises(ApiError) as e:
        join_request.request_join(outing.id)

    assert e.value.status == 401
    assert e.value.code == "unauthorized"

