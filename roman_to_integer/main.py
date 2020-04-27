VALUE_MAP = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_integer(roman):
    if len(roman) == 0:
        return 0
    elif len(roman) >= 2 and VALUE_MAP[roman[0]] < VALUE_MAP[roman[1]]:
        return VALUE_MAP[roman[1]] - VALUE_MAP[roman[0]] + roman_to_integer(roman[2:])
    else:
        return VALUE_MAP[roman[0]] + roman_to_integer(roman[1:])
