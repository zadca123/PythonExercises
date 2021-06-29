#!/usr/bin/env python


def bank_acc(s):
    stored = 0
    L = s.split()
    for i in range(len(L)):
        if i % 2 == 0:
            if L[i] == "D":
                stored += int(L[i + 1])
            elif L[i] == "W":
                stored -= int(L[i + 1])
    return stored


a = input("Type digits separated by coma ',': ")
# a = "D 200 W 300 D 300 W 4300"

print(bank_acc(a))
