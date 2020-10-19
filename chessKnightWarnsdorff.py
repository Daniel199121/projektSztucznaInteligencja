from heapq import heappush, heappop

def skoczek(move, pos_x, pos_y):
    cbx = 8; cby = 8 # width and height of the board
    cb = [[0 for x in range(cbx)] for y in range(cby)] #init board
    # move_x and move_y define next move of Knight.
    # move_x is for next value of x coordinate
    # move_y is for next value of y coordinate
    move_x = [1, 2, 2, 1, -1, -2, -2, -1]
    move_y = [-2, -1, 1, 2, 2, 1, -1, -2]
    # start the Knight from a random position
    if move >= 0 and move < 8:
        # first cell if
        if pos_x >= 0 and pos_x < cbx and pos_y >= 0 and pos_y < cby:
            cb[pos_x][pos_y] = 1
            kx = pos_x + move_x[move]
            ky = pos_y + move_y[move]
            # second cell if
            if kx >= 0 and kx < cbx and ky >= 0 and ky < cby:
                for k in range(64):
                    cb[kx][ky] = k + 2
                    # priority queue of available neighbors
                    pq = []
                    for i in range(8):
                        nx = kx + move_x[i]; ny = ky + move_y[i]
                        if nx >= 0 and nx < cbx and ny >= 0 and ny < cby:
                            if cb[nx][ny] == 0:
                                # count the available neighbors of the neighbor
                                ctr = 0
                                for j in range(8):
                                    ex = nx + move_x[j]; ey = ny + move_y[j]
                                    if ex >= 0 and ex < cbx and ey >= 0 and ey < cby:
                                        if cb[ex][ey] == 0: ctr += 1
                                heappush(pq, (ctr, i))
                    # move to the neighbor that has min number of available neighbors
                    if len(pq) > 0:
                        (p, m) = heappop(pq)
                        kx += move_x[m]; ky += move_y[m]
                    else: break

                #create check table
                table = [[-1 for i in range(8)] for i in range(8)]
                i = 1
                licznik = 0
                for cy in range(8):
                    for cx in range(8):
                        table[cx][cy] = i
                        i += 1

                # print cb
                for cy in range(8):
                    for cx in range(8):
                        print(str(cb[cx][7-cy]), end=' ')
                        for i in range(8):
                            for j in range(8):
                                if table[i][j] == cb[cx][cy]:
                                    licznik += 1
                    print()
                #check correct filling
                #if licznik == 64:
                    #print("Wszystko OK")
            else:
                print("X, Y after move out of bounds")
        else:
            print("X, Y out of bounds")
    else:
        print("Mov out of bounds")

print("-----ZADANIE_3-----")
print("-------PROBLEM SKOCZKA SZACHOWEGO - WARNSDORFF-------")
#Single example
skoczek(2, 0, 0)

'''Generate each possible solution
i = 1
for c in range(8):
    for b in range(8):
        for a in range(8):
            print("------" + str(i)+". SOLUTION FOR: a= "+str(a)+", b= "+str(b)+", c= "+str(c) + "------")
            i += 1
            skoczek(a, b, c)'''