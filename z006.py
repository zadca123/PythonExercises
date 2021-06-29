#!/usr/bin/env python
import math


def something(d):
    c = 50
    h = 30
    return math.sqrt((2 * c * d) / h)


d = int(input("Type the number: "))
print(something(d))
