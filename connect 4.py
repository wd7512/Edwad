import numpy as np
import random

width = 7
height = 6
board = np.zeros([height, width])

def findY(c):
    for i in range(height):
        if(board[height - i - 1][c] == 0):
            return height - i - 1

def randomMove():
    c = random.randint(0, width - 1)
    board[findY(c)][c] = 1

def playerMove():
    c = int(input()) - 1
    board[findY(c)][c] = 2

def checkSame(c1, c2, c3, c4):
    if(c1 != 0 and c1 == c2 and c2 == c3 and c3 == c4):
        return c1
    else:
        return 0

def checkWin():
    # horizontal check
    for i in range(width - 4):
        for j in range(height):
            c1 = board[j][i]
            c2 = board[j][i + 1]
            c3 = board[j][i + 2]
            c4 = board[j][i + 3]

            return checkSame(c1, c2, c3, c4)

    # vertical check
    for i in range(width):
        for j in range(height - 4):
            c1 = board[j][i]
            c2 = board[j + 1][i]
            c3 = board[j + 2][i]
            c4 = board[j + 3][i]

            return checkSame(c1, c2, c3, c4)

    # diagonal check 1
    for i in range(width - 4):
        for j in range(height - 4):
            c1 = board[j][i]
            c2 = board[j + 1][i + 1]
            c3 = board[j + 2][i + 2]
            c4 = board[j + 3][i + 3]

            return checkSame(c1, c2, c3, c4)

    # diagonal check 2
    for i in range(width - 4):
        for j in range(height - 4):
            c1 = board[j][i]
            c2 = board[j + 1][i - 1]
            c3 = board[j + 2][i - 2]
            c4 = board[j + 3][i - 3]

            return checkSame(c1, c2, c3, c4)

def show():
    print(board)

done = False
while not done:
    randomMove()
    show()
    playerMove()
    
    if(checkWin() == 1):
        print("Computer Wins!")
        done = True
    elif(checkWin() == 2):
        print("You Win!")
        done = True
