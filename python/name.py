import sys

while True:
    response = input("Enter a valid option:\n")
    if response == 'exit':
        sys.exit()
        print('You typed {}'.format(response))
