#check if coordinates are in bounds
def validatePosition(x, y, board):
    if (x >= 0 and y >= 0 and x < 8 and y < 8 and board[x][y] == -1):
        return True
    return False

#print board
def printBoard(board):
    for j in range(8):
        for i in range(8):
            print(board[i][7-j], end=' ')
        print()

#define skoczek
def skoczek(move, first_x, first_y):

    # board initialization
    board = [[-1 for i in range(8)] for i in range(8)]

    # move_x and move_y define next move of Knight.
    # move_x is for next value of x coordinate
    # move_y is for next value of y coordinate
    move_x = [1, 2, 2, 1, -1, -2, -2, -1]
    move_y = [-2, -1, 1, 2, 2, 1, -1, -2]

    # first cell if
    if move >= 0 and move < 8:
        if validatePosition(first_x, first_y, board):
            board[first_x][first_y] = 1
            # Second cell attributes
            second_x = first_x + move_x[move]
            second_y = first_y + move_y[move]

            if validatePosition(second_x, second_y, board):
                board[second_x][second_y] = 2
                # Step counter for knight's position
                pos = 3

                # Checking if solution exists or not
                if (not backtracking(board, second_x, second_y, move_x, move_y, pos)):
                    print("Solution does not exist")
                else:
                    print("----------FINAL SOLUTION----------------")
                    printBoard(board)
            else:
                print("X, Y after move out of bounds")
        else:
            print("X, Y out of bounds")
    else:
        print("Mov out of bounds")

def backtracking(board, curr_x, curr_y, move_x, move_y, pos):

    if (pos == ((8 ** 2) + 1)):
        return True

    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if (validatePosition(new_x, new_y, board)):
            board[new_x][new_y] = pos
            if (backtracking(board, new_x, new_y, move_x, move_y, pos + 1)):
                return True

            # Backtracking
            board[new_x][new_y] = -1
    return False

print("-----ZADANIE_2-----")
print("-------PROBLEM SKOCZKA SZACHOWEGO-------")
#Single example
skoczek(2, 0, 0)

'''Generate ech possible solution
i = 1
for c in range(8):
    for b in range(8):
        for a in range(8):
            #IF which not include a few examples recognized as a BIG Time Consuming
            if not ((a==3 and b==0 and c==0) or (a==2 and b==2 and c==0)):
                print("------" + str(i)+". SOLUTION FOR: a= "+str(a)+", b= "+str(b)+", c= "+str(c)+ "------")
                i += 1
                skoczek(a, b, c)
            else:
                print("------" + str(i)+". LEAVE SOLUTION FOR: a= "+str(a)+", b= "+str(b)+", c= "+str(c)+ "------")'''