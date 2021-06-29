#!/usr/bin/env python

f = open("lol.txt", "w")
f.write("hello,nigger")
f.close()

f = open("lol.txt")
text = f.read()
print(type(text))
print(text.split(","))
