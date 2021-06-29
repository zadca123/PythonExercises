#!/usr/bin/env python


def foo(s):
    lett = 0
    dig = 0
    for c in s:
        if c in "0123456789":
            dig += 1
        elif c.lower() in "abcdefghijklmnopqrstuvwxyz":
            lett += 1
    return "LETTERS: " + str(lett) + "\nDIGITS: " + str(dig)


a = input("Type something: ")
print(foo(a))
