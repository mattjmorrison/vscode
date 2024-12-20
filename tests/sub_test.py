import pytest
from app.sub import sub


@pytest.mark.parametrize(
    "a, b, c",
    (
        (1, 2, -1),
        (2, 3, -1),
        (3, 4, -1),
    ),
)
def test_subtraction(a: int, b: int, c: int):
    assert sub(a, b) == c
