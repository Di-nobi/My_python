import os

def func():
    global X
    X = 99
    return X
func()
print(X)
