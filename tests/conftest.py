import httpx
import pytest

from muster_pytest.outings import OutingClient

BASE_URL = "http://localhost:8088/api"


@pytest.fixture
def api():
    client = httpx.Client(base_url=BASE_URL)
    yield client
    client.close()


@pytest.fixture
def outings(api):
    return OutingClient(api)
