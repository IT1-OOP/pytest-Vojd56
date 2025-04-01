from src import calculator
import pytest

@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, -3, 2, (2.0, 1.0)),
        (1, -2, 1, (1.0, 2.0)),
        (2, -7, 3, (3.0, 0.2)),
        (1, 0, -4, (2.0, -2.0)),
    ],
)
def test_correct_solutions(a, b, c, expected):
    assert calculator.solve_quadratic_formula(a, b, c) == expected

@pytest.mark.parametrize(
    "a, b, c, exception",
    [
        ("a", 2, 3, TypeError),
        (1, [2], 3, TypeError),
        (1, 2, None, TypeError),
        (0, 2, 3, SyntaxError),
        (1, 2, 5, ValueError),
        (1, 5, 2, NameError),
    ],
)
def test_exceptions(a, b, c, exception):
    with pytest.raises(exception):
        calculator.solve_quadratic_formula(a, b, c)