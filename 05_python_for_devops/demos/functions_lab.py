# Instructor solutions


def calculate(op_a, op_b, operator):
    """Given two operands and an operator, return
    the result of the operation"""
    if operator == "+":
        return op_a + op_b
    if operator == "-":
        return op_a - op_b
    if operator == "*":
        return op_a * op_b
    if operator == "/":
        return op_a / op_b
    return None


def sumdigits(number):
    """Given an integer, sum the digits and repeat until a single-digit
    value is found"""
    num = number
    while True:
        digits = str(int(num))
        if len(digits) == 1:
            break
        num = sum([int(d) for d in digits])
        print(digits, "summed is", num)
    return num


def add_commas(number):
    """Given an integer, add comma separators for every 3 digit groups"""
    digits = str(int(number))
    digits_rev = list(reversed(digits))
    sections = [
        ''.join(digits_rev[i:i+3])
        for i in range(0, len(digits), 3)]
    result = ','.join(sections)
    return result[::-1]


def collatz(number):
    """Demonstrate the Collatz Conjecture"""
    while number > 1:
        print(number, end=' ')
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
    return number
