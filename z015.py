#!/usr/bin/env python


# def words_sep(n):
#     L = n.split()
#     L.sort()
#     for item in L:
#         if L.count(item) != 1:
#             L.remove(item)
#     return L


def words_sep(n):
    L = n.split()
    L = list(set(L))
    L.sort()
    return L


# a = input("Type the separated by space ' ': ")
a = "hello world and practice makes perfect and hello world again"
print(words_sep(a))
