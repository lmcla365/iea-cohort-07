from fizzbuzz import fizzbuzz


def test_fizzbuzz_number_is_int():
    result = fizzbuzz(1)
    assert type(result) is int

def test_fizzbuzz_multiple_is_str():
    result = fizzbuzz(15)
    assert type(result) is str

