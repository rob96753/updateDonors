#! /usr/bin/python3

# Mod11 algorithm deduced by Andy Hart
def mod_11_algorithm(digits):
    if len(digits) < 1:
        raise IndexError('Input Digits Must Be Of Length 1 or More (mod_11_algorithm)')
    weighting = [2, 3, 4, 5, 6, 7,
                 2, 3, 4, 5, 6, 7,
                 2, 3, 4, 5, 6, 7,
                 2, 3, 4, 5, 6, 7]
    # reverse the string
    reversed = digits[::-1]
    sum = 0
    # step through the digits without the check digit
    # calculating the weighted accumulation
    for i in range(len(reversed)):
        sum += (int(reversed[i]) * weighting[i])

    # the remainder
    remainder = sum % 11

    # concatenate the remainder
    if remainder == 0:
        result = '0'
    elif remainder == 1:
        result = '0'
    else:
        check_digit = 11 - remainder
        result = str(check_digit)

    return result