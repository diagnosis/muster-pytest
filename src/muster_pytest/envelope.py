from typing import Any, cast

import httpx
from pydantic import BaseModel


def unwrap(res: httpx.Response, expected: int = 200) -> dict | None:
    if res.status_code != expected:
        raise AssertionError(
            f"expected status:{expected}, got {res.status_code}. error:{res.text}"
        )
    if not res.content:
        return None
    body = res.json()
    return body.get("data", body)

def unwrap_as[T: BaseModel](resp: httpx.Response, model: type[T], expected:int = 200)-> T :
    data = unwrap(resp, expected)
    if resp.is_success:
        return model.model_validate(data)
    return cast(T, data)