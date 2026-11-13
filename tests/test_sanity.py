def double(n: int) -> int:
    return n * 2


def test_double():
    assert double(2) == 4


def test_double_fails_on_purpose():
    assert double(3) != 7
