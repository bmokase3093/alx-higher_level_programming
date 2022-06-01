#!/usr/bin/python3
def print_last_digit(number):
    l_digit = str(number)[-1]
    l_digit = int(l_digit)
    print(f"{l_digit:d}", end="")
    return (l_digit)
