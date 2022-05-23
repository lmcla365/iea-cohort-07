# Instructor solution

# GOAL:
# Given an Arabic number, transform into Roman numerals
# I II III IV V VI VII VIII IX
# Account for special cases, i.e. 4 = IV, 5 = V, 6 = VI

# Roman digit map for primary decimal places
arabic_to_roman = {
    1: "I",
    10: "X",
    100: "C",
    1000: "M",
}
# Special roman digits for 5x decimal places
five_based = {
    5: "V",
    50: "L",
    500: "D",
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
    # Handle special cases for 4, 9, and >= 5 digits for this place
    if place_value == 4:
        five_digit = five_based.get(5 * divisor)
        if not five_digit:
            print(f"No Roman numeral for {5 * divisor}")
            break
        roman_digits.append(digit + five_digit)
    elif place_value == 9:
        next_digit = arabic_to_roman[10 * divisor]
        if not next_digit:
            print(f"No Roman numeral for {10 * divisor}")
            break
        roman_digits.append(digit + next_digit)
    elif place_value >= 5:
        five_digit = five_based[5 * divisor]
        if not five_digit:
            print(f"No Roman numeral for {5 * divisor}")
            break
        roman_digits.append(five_digit + (digit * (place_value - 5)))
    else:
        roman_digits.append(digit * place_value)

roman = ''.join(roman_digits)
print(f"The number {arabic} in Roman numerals is {roman}")
