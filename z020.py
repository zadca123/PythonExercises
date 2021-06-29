#!/usr/bin/env python


def foo(s):
    up = 0
    low = 0
    for c in s:
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            up += 1
        elif c in "abcdefghijklmnopqrstuvwxyz":
            low += 1
    return "UPPER CASE:\t" + str(up) + "\nLOWER CASE:\t" + str(low)


a = input("Type something: ")
print(foo(a))
