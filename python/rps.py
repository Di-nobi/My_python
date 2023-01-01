import random
import sys

print('Rock, Paper, Scissors')
loss = 0
win = 0
tie = 0
while True:
    print('%s Win, %s Loss, %s Ties' % (win, loss, tie))
while True:
    print('Enter an input: rock, paper, scissor')
    userin = input()
    if userin == 'q': sys.exit()

    if userin == 'r' or userin == 'p' or userin == 's':
        break
    print('select one of r, p, s')

    if userin == 'r':
        print('Rock vs ...')
    elif userin == 'p':
        print('Paper vs ...')
    elif userin == 's':
        print('Scissors vs ...')

        randomnum = random.randint(1, 3)

        if randomnum == 1:
            move = 'r'
            print("Rock")
        elif randomnum == 2:
            move = 'p'
            print("Paper")
        elif randomnum == 3:
            move = 's'
            print("Scissor")

            if userin == move:
                print('A tie')
                tie += 1

            elif userin == 'r' and move == 's':
                print('You win')
                win += 1
            elif userin == 's' and move == 'r':
                print('You lose')
                loss += 1
            elif userin == 'p' and move == 'r':
                print('You win')
                win += 1
            elif userin == 'r' and move == 'p':
                print('You lose')
                loss += 1
            elif userin == 's' and move == 'p':
                print('You win')
                win += 1
            elif userin == 'p' and move == 's':
                print('You lose')
                loss += 1
