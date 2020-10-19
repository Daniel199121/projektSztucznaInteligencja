k = 1
# print board
def printBoard(board, n):
    global k
    print("-------------------SOLUTION " + str(k) + "-------------------")
    k = k + 1
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print("\n")
    print("\n")

#check if coordinates are in proper place - dont cross the laws of the algorithm, this function is called when "col" hetmans are already placed in columns from 0 to col -1.
# So we need to check only left side for attacking hetmans
def validatePosition(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if (board[row][i]):
            return False

    # Check upper diagonal on left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if (board[i][j]):
            return False;
        i -= 1
        j -= 1

    # Check lower diagonal on left side
    i = row
    j = col
    while j >= 0 and i < n:
        if (board[i][j]):
            return False
        i = i + 1
        j = j - 1

    return True

#check placing all available hetmans
def checkPlacing(board, col, n):
    if (col == n):
        printBoard(board, n)
        return True

    #Consider this column and try placing this hetman in all rows one by one
    res = False
    for i in range(n):

        #Check if hetman can be placed on board[i][col]
        if (validatePosition(board, i, col, n)):
            # Place this hetman in board[i][col]
            board[i][col] = 1;

            # Make result true if any placement is possible
            res = checkPlacing(board, col + 1, n) or res;

            # If placing hetman in board[i][col] doesn't lead to a solution, then hetman from board[i][col]
            board[i][col] = 0  # BACKTRACK

    # if the hetman can not be placed in any row in
    return res

def hetmani(n):
    if n > 0:
        board = [[0 for i in range(n)] for i in range(n)]

        if checkPlacing(board, 0, n) == False:
            print("Solution does not exist")
            return
        return
    else:
        print("N out of bounds")

print("-----ZADANIE_5-----")
print("-------PROBLEM OŚMIU HETMANÓW - WSZYSTKIE ROZWIĄZANIA DLA N-------")
#Single example
hetmani(5)

'''Generate more examples - standard for 20 examples
for n in range(1, 21):
    print("----------SOLUTION FOR " + str(n) + " COLUMNS AND RAWS -------------------")
    hetmani(n)'''