import httpx

from muster_pytest.envelope import unwrap


class OutingClient:
    def __init__(self, http: httpx.Client):
        self.http = http

    def browse(
        self,
        limit: int | None = None,
        after: str | None = None,
        *,
        expected: int = 200,
    ) -> dict | None:
        params = {}
        if limit is not None:
            params["limit"] = limit
        if after is not None:
            params["after"] = after
        resp = self.http.get("/outings", params=params)
        return unwrap(resp, expected)
