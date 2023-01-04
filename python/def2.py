#try and except update
def spam(divideBy):
    return 42 / divideBy
try:
   print(spam(2))
   print(spam(12))
   print(spam(0))
except ZeroDivisionError:
    print("Error: Invalid argument")
