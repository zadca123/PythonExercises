#!/usr/bin/env python
import math


def sphereVolume(r):
    return 4 / 3 * math.pi * r ** 3


a = int(input("Type the number: "))
print(sphereVolume(a))
