import random

se.number = random.randint(1, 20)
print('Thinking of a number between 1 to 20')

for guessinput in range(1, 8):
    print('Take a guess')
    guess = int(input())
