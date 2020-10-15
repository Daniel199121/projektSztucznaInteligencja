# Python3 program to solve Knight Tour problem using Backtracking

# Chessboard Size


def isSafe(x, y, board):
    '''
        A utility function to check if i,j are valid indexes
        for N*N chessboard
    '''
    if (x >= 0 and y >= 0 and x < 8 and y < 8 and board[x][y] == -1):
        return True
    return False


def printSolution(board):
    '''
        A utility function to print Chessboard matrix
    '''
    for j in range(8):
        for i in range(8):
            print(board[i][7-j], end=' ')
        print()


def solveKT(move, first_x, first_y):
    '''
        This function solves the Knight Tour problem using
        Backtracking. This function mainly uses solveKTUtil()
        to solve the problem. It returns false if no complete
        tour is possible, otherwise return true and prints the
        tour.
        Please note that there may be more than one solutions,
        this function prints one of the feasible solutions.
    '''

    # Initialization of Board matrix
    board = [[-1 for i in range(8)] for i in range(8)]

    # move_x and move_y define next move of Knight.
    # move_x is for next value of x coordinate
    # move_y is for next value of y coordinate
    move_x = [1, 2, 2, 1, -1, -2, -2, -1]
    move_y = [-2, -1, 1, 2, 2, 1, -1, -2]
    # Since the Knight is initially at the first block
    if move >= 0 and move < 8:
        if isSafe(first_x, first_y, board):
            board[first_x][first_y] = 1
            # Second cell atributes
            second_x = first_x + move_x[move]
            second_y = first_y + move_y[move]
            #print(second_x)
            #print(second_y)

            if isSafe(second_x, second_y, board):
                board[second_x][second_y] = 2
                # Step counter for knight's position
                pos = 3

                # Checking if solution exists or not
                if (not solveKTUtil(board, second_x, second_y, move_x, move_y, pos)):
                    print("Solution does not exist")
                else:
                    print("----------FINAL SOLUTION----------------")
                    printSolution(board)
            else:
                print("X, Y after move out of bounds")
        else:
            print("X, Y out of bounds")
    else:
        print("Mov out of bounds")

def solveKTUtil(board, curr_x, curr_y, move_x, move_y, pos):
    '''
        A recursive utility function to solve Knight Tour
        problem
    '''

    if (pos == 8 ** 2):
        return True

    # Try all next moves from the current coordinate x, y
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if (isSafe(new_x, new_y, board)):
            #print("For position: " + str(pos) + "new coordination are: " + str(new_x) + " and " + str(new_y))
            board[new_x][new_y] = pos
            if (solveKTUtil(board, new_x, new_y, move_x, move_y, pos + 1)):
                return True

            # Backtracking
            board[new_x][new_y] = -1
            counter = 0
            for j in range(8):
                for i in range(8):
                    if board[i][j] != -1:
                        counter += 1
            if counter > 61:
                print("--------------------------")
                printSolution(board)

    return False

solveKT(0, 0, 0)
'''i = 1
for a in range(8):
    for b in range(8):
        for c in range(8):
            print(str(i)+". SOLUTION FOR: a= "+str(a)+", b= "+str(b)+", c= "+str(c))
            i += 1
            solveKT(a, b, c)'''