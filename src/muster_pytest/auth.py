import httpx


class AuthClient:
    def __init__(self, http: httpx.Client):
        self.http = http

    def signup(
        self,
        email: str,
        name: str,
        password: str = "Passw0rd!123",
        experience: str = "beginner",
    ) -> dict:
        resp = self.http.post(
            "/auth/signup",
            json={
                "email": email,
                "name": name,
                "password": password,
                "experience": experience,
            },
        )
        assert resp.status_code == 201, resp.text
        return resp.json()["data"]
