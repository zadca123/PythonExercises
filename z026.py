#!/usr/bin/env python
import math as m


class robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        # self.x = x
        # self.y = y

    def position(self):
        print("os x: ", self.x)
        print("os y: ", self.y)

    def left(self, n):
        if type(n) is not type(int()):
            n = round(n)
        self.x -= n
        print("LEFT ", n)

    def right(self, n):
        if type(n) is not type(int()):
            n = round(n)
        self.x += n
        print("RIGHT", n)

    def up(self, n):
        if type(n) is not type(int()):
            n = round(n)
        self.y += n
        print("UP ", n)

    def down(self, n):
        if type(n) is not type(int()):
            n = round(n)
        self.y -= n
        print("DOWN ", n)

    def distance(self):
        print(
            "Distance from (0,0) to ({},{}) is: {}".format(
                self.x, self.y, m.sqrt(self.x ** 2 + self.y ** 2)
            )
        )


# n = input("Type some number: ")
r = robot()
r.position()
r.right(3)
r.up(4)
r.position()
r.distance()
