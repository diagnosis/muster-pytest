import httpx

from muster_pytest.envelope import unwrap


class JoinRequestClient:
    def __init__(self, http: httpx.Client):
        self.http = http

    def request_join(
        self, outing_id: str, *, expected: int = 201, **overrides
    ) -> dict | None:
        resp = self.http.post(
            f"/outings/{outing_id}/requests",
            json={"role": "rider", "seats_offered": 0, "guests": 0, **overrides},
        )
        return unwrap(resp, expected=expected)

    def accept(self, request_id: str, *, expected: int = 200) -> dict | None:
        resp = self.http.post(f"/requests/{request_id}/accept")
        return unwrap(resp, expected=expected)

    def withdraw(self, outing_id: str, *, expected: int = 200) -> dict | None:
        resp = self.http.delete(f"/outings/{outing_id}/requests/me")
        return unwrap(resp, expected=expected)

    def decline(self, request_id: str, *, expected: int = 200) -> dict | None:
        resp = self.http.post(f"/requests/{request_id}/decline")
        return unwrap(resp, expected)
