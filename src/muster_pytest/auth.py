import httpx

from muster_pytest.envelope import unwrap


class AuthClient:
    def __init__(self, http: httpx.Client):
        self.http = http

    def signup(
        self,
        email: str,
        name: str,
        password: str = "Passw0rd!123",
        experience: str = "beginner",
        *,
        expected: int = 201,
    ) -> dict | None:
        resp = self.http.post(
            "/auth/signup",
            json={
                "email": email,
                "name": name,
                "password": password,
                "experience": experience,
            },
        )
        return unwrap(resp, expected)

    def verify_email(self, token: str, *, expected: int = 200) -> dict | None:
        resp = self.http.post("/auth/verify-email", json={"token": token})
        return unwrap(resp, expected)

    def login_with_password(
        self, email: str, password: str = "Passw0rd!123", *, expected: int = 200
    ) -> dict | None:
        resp = self.http.post(
            "/auth/login", json={"email": email, "password": password}
        )
        return unwrap(resp, expected)
