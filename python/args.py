#!/usr/bin/python3
if __name__ == "__main__":
    import sys
n = len(sys.argv) - 1
i = 0
if n == 0:
    print("{} arguments.".format(n))
elif n == 1:
    print("{} argument:".format(n))
else:
    print("{} arguments:".format(n))
    for args in n:
        if i != 0:
            print("{} argument:".format(i, args))
            i += 1

