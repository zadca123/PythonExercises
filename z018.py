#!/usr/bin/env python


def expand(s):
    L = []
    for c in s:
        if c not in "0123456789":
            L.append(c)
            mem = c
        else:
            for x in range(int(c)):
                L.append(mem)
    return "".join(L)


# def shorten(s):
#     L = list(s)
#     index = 0
#     for i in range(len(L)):
#         if i > 0:
#             if L[i] == L[i - 1]:
#                 L.remove(L[i])
#                 print("popped: " + L[i])
#     return "".join(L)


def shorten(s):
    L = list(s)
    res = []
    mem = 1
    for i in range(len(L)):
        if L[i - 1] != L[i]:
            res.append(str(mem))
            res.append(L[i])
            mem = 1
        else:
            mem += 1
    x = str("".join(res))
    return x[1:] + x[0]


a = "a2b3c1"
print(expand(a))
a = "bbbbbcccaaa"
print(shorten(a))
# print(int(Decimala[0]))
