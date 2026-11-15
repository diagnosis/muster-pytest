from dataclasses import dataclass

import httpx

from muster_pytest.auth import AuthClient
from muster_pytest.db import mint_verification_token
from muster_pytest.identity import unique_identity
from muster_pytest.join_requests import JoinRequestClient
from muster_pytest.outings import OutingClient
from muster_pytest.schemas import Hiker


@dataclass
class Actor:
    http: httpx.Client
    hiker: Hiker
    email: str
    auth: AuthClient
    outings: OutingClient
    join_requests: JoinRequestClient


def create_actor(base_url: str) -> Actor:
    http = httpx.Client(base_url=base_url)
    auth = AuthClient(http)
    name, email = unique_identity()
    hiker = auth.signup(email=email, name=name)
    tok = mint_verification_token(hiker.id)
    auth.verify_email(token=tok, expected=200)
    hiker = auth.login_with_password(email=email)
    return Actor(
        http=http,
        hiker=hiker,
        email=email,
        auth=auth,
        outings=OutingClient(http),
        join_requests=JoinRequestClient(http),
    )
