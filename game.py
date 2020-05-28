import math
import random


def printBoard(board):
    count = 1
    for i in range(3):
        for j in range(3):
            char = board[i][j]
            if board[i][j] == '   ':
                char = ' ' + str(count) + ' '
            if j != 2:
                print(char, end='|')
            else:
                print(char, end='')
            count+=1
        if i != 2:
            print("\n-----------")
    print()

def isDiagDown(board, mark):

    for i in range(3):

        if board[i][i]!= mark:
            return False
    return True


def isDiagUp(board, mark):
    for i in range(3):
        if board[2-i][i] != mark:
            return False
    return True

def isVertical(board, j, mark):
    #print("in vertical")
    for i in range(3):
        #print(i, ", ", j)
        if board[i][j] != mark:
            return False
    return True

def isHorizontal(board, i, mark):
    for j in range(3):
        if board[i][j] != mark:
            return False
    return True


def isWin(board, i, j, mark):
    if isVertical(board, j, mark):
        return True
    if isHorizontal(board, i, mark):
        return True

    if i == j or 2-i == j:
        if isDiagUp(board, mark):
            return True
        if isDiagDown(board, mark):
            return True

    #print("No win for ", mark)
    return False


def playerTurn(board):
    #asking for input
    n = input("Enter box to mark [1..9]: ")
    while not str.isdigit(n) or int(n) > 9:
        print("You can only enter 1, 2, 3, 4, 5, 6, 7, 8 or 9")
        n = input("Enter a valid number: ")

    n=int(n)
    r = n//3
    c = n%3 - 1
    if c==-1:
        r= r-1
        c=2


    while board[r][c] != '   ':
        print("Positions already marked")
        n = input("Enter a valid number: ")
        while not str.isdigit(n) or int(n) > 2:
            print("You can only enter 1, 2, 3, 4, 5, 6, 7, 8 or 9")
            n = input("Enter a valid number: ")
        n=int(n)
        r = n // 3
        c = n % 3 - 1
        if c == -1:
            r = r - 1
            c = 2




    board[r][c] = ' o '
    return isWin(board, r, c, ' o ')

def computerTurn(board):

    #computation
    n = random.randint(1,9)
    n = int(n)
    r = n // 3
    c = n % 3 - 1
    if c == -1:
        r = r - 1
        c = 2

    while board[r][c] != '   ':
        n = random.randint(1, 9)
        n = int(n)
        r = n // 3
        c = n % 3 - 1
        if c == -1:
            r = r - 1
            c = 2
    #mark
    board[r][c] = ' x '
    return isWin(board, r, c, ' x ')





board = []
for i in range(3):
    board.append([])
    for j in range(3):
        board[i].append("   ")

printBoard(board)

winner = None

markedBoxes = 0
while winner == None:
    if playerTurn(board):
        winner = "Human wins"
        break
    markedBoxes+=1
    if markedBoxes == 9:
        winner = "Tie"
        break

    if computerTurn(board):
        winner = "Computer wins"
    markedBoxes+=1

    printBoard(board)

print(winner)








