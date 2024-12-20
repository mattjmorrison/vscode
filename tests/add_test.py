import pytest
from app.add import add


@pytest.mark.parametrize(
    "a, b, c",
    (
        (1, 2, 3),
        (2, 3, 5),
        (3, 4, 7),
    ),
)
def test_addition(a: int, b: int, c: int):
    assert add(a, b) == c
