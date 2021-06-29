#!/usr/bin/env python


def foo(x, y):
    L = []
    for i in range(x):
        x = []
        for j in range(y):
            x.append(i * j)
        L.append(x)
    print(L)
    return L


x = int(input("Type number (1): "))
y = int(input("Type number (2): "))
foo(x, y)
