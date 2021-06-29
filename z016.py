#!/usr/bin/env python


def binarny(n):
    L = n.split(",")
    i = 0
    for b in L:
        if int(b, 2) % 5 == 0:
            print(L[i])
        i += 1
    return L


# a = input("Type the separated by space ' ': ")
a = "1010,0101,0011,0001"
print(binarny(a))
