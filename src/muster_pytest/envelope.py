import httpx
from pydantic import BaseModel


def unwrap(res: httpx.Response, expected: int = 200) -> dict | None:
    if not res.is_success:
        error = res.json()["error"]
        raise ApiError(res.status_code, error["code"], error["message"])
    if res.status_code != expected:
        raise AssertionError(
            f"expected status:{expected}, got {res.status_code}. body:{res.text}"
        )
    if not res.content:
        return None
    body = res.json()
    return body.get("data", body)


def unwrap_as[T: BaseModel](
    resp: httpx.Response, model: type[T], expected: int = 200
) -> T:
    return model.model_validate(unwrap(resp, expected))


class ApiError(Exception):
    def __init__(self, status: int, code: str, message: str):
        super().__init__(f"{status} {code}: {message}")
        self.status = status
        self.code = code
        self.message = message
