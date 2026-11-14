from muster_pytest.identity import unique_identity


def test_signup_returns_hiker(auth):
    name, email = unique_identity()
    hiker = auth.signup(email, name)
    assert hiker["id"]
    assert hiker["email"] == email
    assert hiker["verified_at"] is None
