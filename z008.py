#!/usr/bin/env python
import math


def search():
    result = []
    for i in range(2000, 3201, 7):
        if i % 5:
            result.append(i)
        return sum(result)


print(search())

L = [i for i in range(2000, 3201, 7) if i % 5]
print(sum(L))
