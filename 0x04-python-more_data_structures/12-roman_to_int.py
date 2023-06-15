#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_number = 0
    numbers = [roman_dict[x] for x in roman_string]
    for i in range(len(numbers)):
        if i > 0 and numbers[i - 1] < numbers[i]:
            roman_number += numbers[i] - 2 * numbers[i - 1]
        else:
            roman_number += numbers[i]
    return roman_number
