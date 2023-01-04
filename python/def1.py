def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
p = spam(2)
x = spam(12)
y = spam(0)

print(p, x, y)
