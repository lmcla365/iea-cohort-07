roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
total_value = 0
entry = "CDLIV"

last = 'M'
entry_list = list(entry)
print(entry_list)
while entry_list:
    for letter in entry_list:
        if roman[letter] <= roman[last]:
            total_value += roman[letter]
#           print(roman[last])
        else:
            total_value +=  roman[letter] -(2 * roman[last])
        last = letter
        print(total_value)
print(total_value)
