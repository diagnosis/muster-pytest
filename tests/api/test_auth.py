from muster_pytest.db import mint_verification_token
from muster_pytest.identity import unique_identity


def test_signup_returns_hiker(auth):
    name, email = unique_identity()
    hiker = auth.signup(email, name)
    assert hiker["id"]
    assert hiker["email"] == email
    assert hiker["verified_at"] is None


def test_signup_verify_login(auth):
    name, email = unique_identity()
    hiker = auth.signup(email, name)
    assert hiker["id"]
    tok = mint_verification_token(hiker["id"], "email_verification", 1)
    auth.verify_email(tok)
    hiker = auth.login_with_password(email)
    assert hiker["verified_at"]


def test_actors_are_isolated(make_actor):
    host = make_actor()
    hiker = make_actor()
    assert host.hiker is not None
    assert hiker.hiker is not None
    assert host.hiker["id"] != hiker.hiker["id"]
    assert host.http.cookies["access_token"] != hiker.http.cookies["access_token"]
