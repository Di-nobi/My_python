#!/usr/bin/python3
def uppercase(c):
    for c in range(97, 123):
        if c >= 97 and c <= 122:
            c = c - 32
uppercase()
print("{:c}".format(c), end="")
