import pytest

from muster_pytest.envelope import ApiError


def test_host_can_create_outing(make_actor):
    host = make_actor()
    outing = host.outings.create(max_size=4)
    assert host.hiker.id == outing.host_id
    assert outing.max_size == 4
    assert outing.status == "open"


@pytest.mark.parametrize(
    "overrides, code",
    [
        pytest.param({"max_size": 0}, "bad_request", id="zero max_size"),
        pytest.param({"title": ""}, "validation_error", id="no title"),
        pytest.param({"host_seats": -1}, "bad_request", id="negative host seats"),
        pytest.param(
            {"starts_at": "2020-01-01T00:00:00Z"}, "bad_request", id="starts at past"
        ),
        pytest.param({"difficulty": "extreme"}, "bad_request", id="wrong difficulty"),
    ],
)
def test_create_rejects_invalid_input(make_actor, overrides, code):
    host = make_actor()
    with pytest.raises(ApiError) as e:
        host.outings.create(**overrides)
    assert code == e.value.code
