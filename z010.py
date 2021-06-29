#!/usr/bin/env python
def idk(n):
    for i in range(1, n + 1):
        print(i, i ** 2, i ** 3)


a = int(input("Type the number: "))
print(idk(a))


# import numpy as np
# def idk(n):
#     L = np.zeros((n, 3))
#     for i in range(1, n):
#         for j in range(3):
#             L[i][j] = i ** (j + 1)
#     return L
# a = int(input("Type the number: "))
# print(idk(a))
