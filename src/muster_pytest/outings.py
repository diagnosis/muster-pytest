import httpx


class OutingClient:
    def __init__(self, http: httpx.Client):
        self.http = http

    def browse(self, limit: int | None = None, after: str | None = None) -> dict:
        params = {}
        if limit:
            params["limit"] = limit
        if after:
            params["after"] = after
        resp = self.http.get("/outings", params=params)
        resp.raise_for_status()
        return resp.json()["data"]
