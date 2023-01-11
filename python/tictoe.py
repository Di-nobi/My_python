theBoard = {'top-L': 'o', 'top-M': 'x', 'top-R': 'x',
'mid-L': ' ', 'mid-M': 'o', 'mid-R': 'x',
'low-L': ' ', 'low-M': ' ', 'low-R': 'o'}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)
