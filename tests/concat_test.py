import pytest
from app.concat import concat


@pytest.mark.parametrize(
    "a, b, c",
    (
        ("1", "2", "12"),
        ("2", "3", "23"),
        ("3", "4", "34"),
    ),
)
def test_concat(a: str, b: str, c: str) -> None:
    assert concat(a, b) == c
