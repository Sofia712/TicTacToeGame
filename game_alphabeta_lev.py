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

        if board[i][i] != mark:
            return False
    return True


def isDiagUp(board, mark):
    for i in range(3):
        if board[2 - i][i] != mark:
            return False
    return True


def isVertical(board, j, mark):
    # print("in vertical")
    for i in range(3):
        # print(i, ", ", j)
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

    if i == j or 2 - i == j:
        if isDiagUp(board, mark):
            return True
        if isDiagDown(board, mark):
            return True

    # print("No win for ", mark)
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


def computerTurn(board, depth, var):
    # selecting best turn

    maxScore = - math.inf
    move_r = -1
    move_c = -1

    for i in range(3):
        for j in range(3):
            if board[i][j] == '   ':
                board[i][j] = ' x '
                score = alphabeta(board, i, j, depth, -math.inf, math.inf, False, var)
                if score > maxScore:
                    move_r = i
                    move_c = j
                    maxScore = score
                board[i][j] = '   '

    board[move_r][move_c] = ' x '
    # mark
    # board[i][j] = ' x '

    return isWin(board, move_r, move_c, ' x ')


def alphabeta(board, move_i, move_j, depth, al, be, isMax, var):
    # computer turn

    if isMax:
        if isWin(board, move_i, move_j, ' o '):
            return -10
    else:
        if isWin(board, move_i, move_j, ' x '):
            return 10
    if depth == 8:
        return 0

    if isMax:
        maxScore = -math.inf

        for row in range(3):
            if maxScore > be:
                break
            for col in range(3):
                if maxScore > be:
                    break
                # else:
                if board[row][col] == '   ':
                    board[row][col] = ' x '
                    sc = alphabeta(board, row, col, depth + 1, maxScore, be, False, var) + random.randint(-var, var)
                    maxScore = max(sc, maxScore)
                    board[row][col] = '   '

        return maxScore

    else:
        minScore = math.inf

        for row in range(3):
            if minScore < al:
                break
            for col in range(3):
                if minScore < al:
                    break
                #    else:
                if board[row][col] == '   ':
                    board[row][col] = ' o '
                    sc = alphabeta(board, row, col, depth + 1, al, minScore, True, var) + random.randint(-var, var)
                    if sc < minScore:
                        minScore = sc

                    board[row][col] = '   '
        return minScore


if __name__ == '__main__':

    d = int(input("Hello, select 0 (easy), 1 (medium) or 2 (hard) to select a difficulty level: "))
    while d>2 or d<0:
        d = int(input("You can only select 0, 1 or 2"))

    if d == 0:
        level = "EASY"
    if d == 1:
        level = "MEDIUM"
    else:
        level= "HARD"
    print("LEVEL: ", level)

    # computing variance according to difficulty selected
    var = (2-d + 1)*4

    board = []
    for i in range(3):
        board.append([])
        for j in range(3):
            board[i].append('   ')

    printBoard(board)

    winner = None

    markedBoxes = 0
    while winner is None:
        if playerTurn(board):
            winner = "Human wins"
            printBoard(board)
            break
        markedBoxes += 1
        if markedBoxes == 9:
            winner = "Tie"
            printBoard(board)
            break

        if computerTurn(board, markedBoxes, var):
            winner = "Computer wins"
        markedBoxes += 1

        printBoard(board)

    print(winner)
