import math


def palindrome_number(num):
    if num < 0:
        return False
    l = length_of_num(num)
    i = 1
    j = l
    palindrome = True
    while i < j and palindrome is True:
        if digit_at_position(num, l, i) != digit_at_position(num, l, j):
            palindrome = False
        i += 1
        j -= 1
    return palindrome


def length_of_num(n):
    if n > 0:
        return int(math.log10(n))+1
    elif n == 0:
        return 1
    else:
        return int(math.log10(-n))+2


def digit_at_position(num, length, position):
    return (num//10 ** (length - position)) % 10
