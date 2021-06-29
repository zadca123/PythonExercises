#!/usr/bin/env python


# def words_sep(n):
#     L = []
#     mem = 0
#     for i in range(len(n)):
#         if n[i] == ",":
#             L.append(n[mem:i])
#             mem = i + 1
#         elif i == (len(n) - 1):
#             L.append(n[mem:])
#     L.sort()
#     return L


def words_sep(n):
    return n.split(",")


# a = input("Type the separated by coma ',': ")
a = "without,hello,bag,world"
print(words_sep(a))
