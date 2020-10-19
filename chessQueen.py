#check if coordinates are in bounds
def printBoard(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

#check if coordinates are in proper place - dont cross the laws of the algorithm
def validatePosition(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

#check placing all available hetmans
def checkPlacing(board, col, n):

    if col >= n:
        return True

    # Consider this column and try placing this hetman in all rows one by one
    for i in range(n):

        if validatePosition(board, i, col, n):

            # Place this hetman in board[i][col]
            board[i][col] = 1

            # recur to place rest of the hetmans
            if checkPlacing(board, col + 1, n) == True:
                return True

            # If placing hetman in board[i][col] doesn't lead to a solution, then hetman from board[i][col]
            board[i][col] = 0

    # if the hetman can not be placed in any row in
    return False

def hetmani(n):
    if n > 0:
        board = [[0 for i in range(n)] for i in range(n)]

        if checkPlacing(board, 0, n) == False:
            print("Solution does not exist")
            return False

        printBoard(board, n)
        return True
    else:
        print("N out of bounds")

print("-----ZADANIE_4-----")
print("-------PROBLEM OŚMIU HETMANÓW-------")
#Single example
hetmani(5)

'''Generate more examples - standard for 20 examples
for n in range(1, 21):
    print("-------------------SOLUTION FOR " + str(n) + " COLUMNS AND RAWS-------------------")
    hetmani(n)'''