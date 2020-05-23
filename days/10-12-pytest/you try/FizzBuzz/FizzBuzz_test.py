import pytest
from FizzBuzz import fizzbuzz


@pytest.mark.parametrize("argument, return_value", [
    (1, 1),
    (2, 2),
    (3, "Fizz"),
    (4, 4),
    (5, "Buzz"),
    (6, "Fizz"),
    (7, 7),
    (8, 8),
    (9, "Fizz"),
    (10, "Buzz"),
    (11, 11),
    (12, "Fizz"),
    (14, 14),
    (15, "FizzBuzz"),
    (16, 16)
])
def test_fizz_buzz(argument, return_value):
    assert fizzbuzz(argument) == return_value
