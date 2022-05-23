import fizzbuzz from fizbuzz

def test_fizzbuzz_three():
    result = fizzbuzz(3)
    return result == 'fizz'

def test_fizzbuzz_five():
    result = fizzbuzz(5)
    return result == 'buzz'

def test_fizzbuzz_fifteen():
    result = fizzbuzz(15)
    return result == 'fizzbuzz'

def test_fizzbuzz_two():
    result = fizzbuzz(2)
    return result == 2
