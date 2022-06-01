#!/usr/bin/python3
def remove_char_at(str, n):
    myString = ""
    for i in range(len(str)):
        if i != n:
            myString = myString + str[i]
    return (myString)
