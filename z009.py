#!/usr/bin/env python
import math


def silnia(n):
    if n <= 1:
        return 1
    return silnia(n - 1) * n


a = int(input("Type the number: "))
print(silnia(a))
