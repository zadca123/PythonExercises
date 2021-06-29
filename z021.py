#!/usr/bin/env python


def foo(s):
    # L = a.split(",")
    # b = [i for i in L if int(i) % 2 == 1]
    b = [i for i in a.split(",") if int(i) % 2 == 1]
    return ", ".join(b)


a = input("Type digits separated by coma ',': ")

print(foo(a))
