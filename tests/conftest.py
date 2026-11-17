import os

import httpx
import pytest

from muster_pytest.actor import create_actor
from muster_pytest.auth import AuthClient
from muster_pytest.outings import OutingClient

BASE_URL = os.environ.get("BASE_URL", "http://localhost:8088/api")


@pytest.fixture
def api():
    client = httpx.Client(base_url=BASE_URL)
    yield client
    client.close()


@pytest.fixture
def outings(api):
    return OutingClient(api)


@pytest.fixture
def auth(api):
    return AuthClient(api)


@pytest.fixture
def make_actor():
    created = []

    def _make():
        actor = create_actor(BASE_URL)
        created.append(actor)
        return actor

    yield _make

    for actor in created:
        actor.http.close()
