#!/usr/bin/python3
def no_c(my_string):
    lisChars = list(my_string)
    for cC in lisChars:
        if cC == 'c' or cC == 'C':
            lisChars.remove(cC)
    return(lisChars)
