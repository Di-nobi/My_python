import random
import sys
secretnumber = random.randint(1, 20)
print('Thinking of a number between 1 to 20')

for guessinput in range(1, 8):
    print('Take a guess')
    guess = int(input())

    if guess < secretnumber:
        print('Guess too low')
    elif guess > secretnumber:
        print('Guess too high')
    else:
        print('you got it dumbass')
        sys.exit()
