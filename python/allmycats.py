Mycats = []
while True:
    print('Enter the name of that scary cat =>' + str(len(Mycats) + 1),'(Or enter nothing.):')
    name = input()
    if name == '':
        break
    Mycats += [name]
    print('The cat names are:')
    for name in Mycats:
        print(' ' + name)
