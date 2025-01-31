import pytest
from app.mul import mul


@pytest.mark.parametrize(
    "a, b, c",
    (
        (1, 2, 2),
        (2, 3, 6),
        (3, 4, 12),
        (4, 5, 20),
        (5, 6, 30),
        (6, 7, 42),
        (7, 8, 56),
        (8, 9, 72),
    ),
)
def test_mul(a, b, c):
    assert mul(a, b) == c
