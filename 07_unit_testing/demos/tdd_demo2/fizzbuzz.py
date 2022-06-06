
def fizzbuzz(num):
    if not num:
        return 0

    result = ''
    if num % 3 == 0:
        result += "fizz"
    if num % 5 == 0:
        result += "buzz"
    if not result:
        result = num

    return result
