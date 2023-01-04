#!/usr/bin/python3

for c in range(97, 123):
    if ord(c) >= 97 and ord(c) < 123:
        char = chr(c) - 32
        print("{}".format(c), end="")
