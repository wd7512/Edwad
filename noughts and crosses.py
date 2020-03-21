from numpy.random import randint

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]   # 0 = nothing, 1 = cpu, 2 = player

def posMove(x, y):
    if(board[x][y] == 0):
        return True
    else:
        return False

def randomMove():
    done = False

    while not(done):
        x = randint(0, 3)
        y = randint(0, 3)
    
        if(posMove(x, y)):
            board[x][y] = 1
            done = True

def playerMove():
    done = False

    while not(done):
        n = int(input())
        
        x = int(n / 3)
        y = n % 3
        
        if(posMove(x, y)):
            board[x][y] = 2
            done = True

def checkWinner():
    for i in range(3):   # check horizontals
        if(board[i] == [1, 1, 1]):
            return 1
        elif(board[i] == [2, 2, 2]):
            return 2

    vcRow = 0
    vpRow = 0
    
    for i in range(3):   # check verticals
        if(board[i][0] == 1):
            vcRow += 1
        elif(board[i][0] == 2):
            vpRow += 1
    if(vcRow == 3):
        return 1
    if(vpRow == 3):
        return 2

    if(board[0][0] == board[1][1] and board[1][1] == board[2][2]):   # check diagonal 1
        return board[0][0]
    if(board[0][2] == board[1][1] and board[1][1] == board[2][0]):   # check diagonal 2
        return board[0][2]

def show():
    print(board[0])
    print(board[1])
    print(board[2])

cont = True
start = 1   # 1 = cpu starts, -1 = player starts

while(cont):
    randomMove()
    show()
    playerMove()

    winner = checkWinner()
    if(winner == 1):
        show()
        print("Computer Wins!")
        cont = False
    elif(winner == 2):
        show()
        print("You Win!")
        cont = False
