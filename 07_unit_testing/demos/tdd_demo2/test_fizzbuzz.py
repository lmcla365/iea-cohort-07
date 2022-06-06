import pytest
from fizzbuzz import fizzbuzz


def test_fizzbuzz_zero():
    number = 0
    result = fizzbuzz(number)

    assert result == number


def test_fizzbuzz_one():
    number = 1
    result = fizzbuzz(number)

    assert result == number


def test_fizzbuzz_three():
    number = 3
    result = fizzbuzz(number)

    assert result == "fizz"


def test_fizzbuzz_five():
    number = 5
    result = fizzbuzz(number)

    assert result == "buzz"


def test_fizzbuzz_six():
    number = 6
    result = fizzbuzz(number)

    assert result == "fizz"


def test_fizzbuzz_ten():
    number = 10
    result = fizzbuzz(number)

    assert result == "buzz"


def test_fizzbuzz_fifteen():
    number = 15
    result = fizzbuzz(number)

    assert result == "fizzbuzz"


def test_fizzbuzz_string_raises_typeerror():
    number = "abc"
    with pytest.raises(TypeError):
        result = fizzbuzz(number)
