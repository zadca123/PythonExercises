#!/usr/bin/env python


class foo:
    def __init__(self, x):
        self.x = x

    def get_string(self):
        return self.x

    def print_string(self):
        print(self.x)


a = input("Type something: ")
print(foo(a).get_string())
print(foo(a).print_string())
