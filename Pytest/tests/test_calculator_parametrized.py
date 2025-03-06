import pytest
from src import calculator


def test_add():
    assert calculator.add(1,2) == 3
    assert calculator.add(0,5) == 5
    assert calculator.add(-2,9) == 7
    assert calculator.add(5, -8) == -3


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (0, 5, 5),
        (-2, 9, 7),
        (5, -8, -3),
    ],
)
def test_add(a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (0, 5, 5),
        (-2, 9, 7),
        (0, 0, 0),
    ],
)
def test_add_wrong(a, b, expected):
    assert calculator.add_wrong(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (0, 5, 0),
        (-2, 4, -8),
        (5, -3, -15),
    ],
)
def test_multiply(a, b, expected):
    assert calculator.multiply(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (0, 5, 0),
        (-2, 4, -8),
        (5, -3, -15),
    ],
)
def test_multiply_wrong(a, b, expected):
    assert calculator.multiply_wrong(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 2, 3),
        (0, 5, -5),
        (-2, 9, -11),
        (7, -3, 10),
    ],
)
def test_subtract(a, b, expected):
    assert calculator.subtract(a, b) == expected