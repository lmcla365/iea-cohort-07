# Instructor solution

# GOAL:
# Given an Arabic number, transform into Roman numerals
arabic_to_roman = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M",
}


# Request a number from the user
arabic = int(input("Please enter a positive integer:"))
value = arabic

roman_digits = []
# Loop from the highest to lowest value places
for divisor in sorted(arabic_to_roman, reverse=True):
    # Figure out the value of this place
    # (i.e. how many repeat roman digits)
    place_value = value // divisor
    # Keep the remainder for the next iteration
    value = value % divisor
    # Short-circuit if the number is less than this divisor
    if place_value < 0:
        continue

    # Look up the roman digits for this divisor
    digit = arabic_to_roman[divisor]
    roman_digits.append(digit * place_value)

roman = ''.join(roman_digits)
print(f"The number {arabic} in Roman numerals is {roman}")
