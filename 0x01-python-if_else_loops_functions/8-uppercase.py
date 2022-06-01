#!/usr/bin/python3
def uppercase(str):
    resul = ''
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            resul += chr(ord(c) - 32)
        else:
            resul += c
    print("{:s}".format(resul))
