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

@pytest.mark.parametrize(
    "a, b, expected_expection, expected_msg",
    [
        (0, 5, ValueError, "Cannot take log of non-positive number!"),
        (-2, 5, ValueError, "Cannot take log of non-positive number!"),
        (9, -2, ZeroDivisionError, "Cannot take log with non-positive base!"),
        (5, 1, NameError, "Cannot take log with base 1!"),
    ],
)
def test_log(a, b, expected_expection, expected_msg):
    with pytest.raises(expected_expection) as exc:
        calculator.log(a, b)
    assert str(exc.value) == expected_msg