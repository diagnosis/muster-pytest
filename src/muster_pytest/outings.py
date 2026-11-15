import httpx

from muster_pytest.envelope import unwrap_as
from muster_pytest.outing_data import unique_outing
from muster_pytest.schemas import Detail, Outing, Page


class OutingClient:
    def __init__(self, http: httpx.Client):
        self.http = http

    def browse(
        self,
        limit: int | None = None,
        after: str | None = None,
        *,
        expected: int = 200,
    ) -> Page:
        params = {}
        if limit is not None:
            params["limit"] = limit
        if after is not None:
            params["after"] = after
        resp = self.http.get("/outings", params=params)
        return unwrap_as(resp, Page, expected)

    def create(self, *, expected: int = 201, **overrides) -> Outing:
        resp = self.http.post("/outings", json=unique_outing(**overrides))
        return unwrap_as(resp, Outing, expected)

    def details(self, outing_id: str, *, expected: int = 200) -> Detail:
        resp = self.http.get(f"/outings/{outing_id}")
        return unwrap_as(resp, Detail, expected)
