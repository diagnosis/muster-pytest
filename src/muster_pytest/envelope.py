import httpx


def unwrap(res: httpx.Response, expected: int = 200) -> dict | None:
    if res.status_code != expected:
        raise AssertionError(
            f"expected status:{expected}, got {res.status_code}. error:{res.text}"
        )
    if not res.content:
        return None
    body = res.json()
    return body.get("data", body)
