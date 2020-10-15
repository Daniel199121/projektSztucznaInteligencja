from heapq import heappush, heappop # for priority queue
import random
import string
def warnsdorfKnightChess(move, pos_x, pos_y):
    cbx = 8; cby = 8 # width and height of the chessboard
    cb = [[0 for x in range(cbx)] for y in range(cby)] # chessboard
    # directions the Knight can move on the chessboard
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    # start the Knight from a random position
    if move >= 0 and move < 8:
        if pos_x >= 0 and pos_x < cbx and pos_y >= 0 and pos_y < cby:
            cb[pos_x][pos_y] = 1
            kx = pos_x + dx[move]
            ky = pos_y + dy[move]
            if kx >= 0 and kx < cbx and ky >= 0 and ky < cby:
                for k in range(64):
                    cb[kx][ky] = k + 2
                    pq = [] # priority queue of available neighbors
                    for i in range(8):
                        nx = kx + dx[i]; ny = ky + dy[i]
                        if nx >= 0 and nx < cbx and ny >= 0 and ny < cby:
                            if cb[nx][ny] == 0:
                                # count the available neighbors of the neighbor
                                ctr = 0
                                for j in range(8):
                                    ex = nx + dx[j]; ey = ny + dy[j]
                                    if ex >= 0 and ex < cbx and ey >= 0 and ey < cby:
                                        if cb[ex][ey] == 0: ctr += 1
                                heappush(pq, (ctr, i))
                    # move to the neighbor that has min number of available neighbors
                    if len(pq) > 0:
                        (p, m) = heappop(pq)
                        kx += dx[m]; ky += dy[m]
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
                if licznik == 64:
                    print("Wszystko OK")
            else:
                print("X, Y after move out of bounds")
        else:
            print("X, Y out of bounds")
    else:
        print("Mov out of bounds")

warnsdorfKnightChess(0, 0, 0)

'''i = 1
for c in range(8):
    for b in range(8):
        for a in range(8):
            print(str(i)+". SOLUTION FOR: a= "+str(a)+", b= "+str(b)+", c= "+str(c))
            i += 1
            warnsdorfKnightChess(a, b, c)'''