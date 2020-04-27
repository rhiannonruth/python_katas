VALUE_MAP = {"V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_integer(roman):
    if len(roman) > 0 and roman[0] in list(VALUE_MAP.keys()):
        return VALUE_MAP[roman[0]] + roman_to_integer(roman[1:])
    if len(roman) > 1 and roman[1] in list(VALUE_MAP.keys()):
        return (VALUE_MAP[roman[1]] - 1) + roman_to_integer(roman[2:])
    return roman.count("I")
