def is_valid(i, j, sol):
  if (i>=0 and i<8 and j>=0 and j<8):
    if (sol[i][j]==-1):
      return True
  return False

def knight_tour(sol, x, y, step_count, x_move, y_move):
  if (step_count == 8*8):
    return True

  for k in range(0, 8):
    next_i = x+x_move[k]
    next_j = y+y_move[k]

    if(is_valid(next_i, next_j, sol)):
      sol[next_i][next_j] = step_count
      if (knight_tour(sol, next_i, next_j, step_count+1, x_move, y_move)):
        print("Póki co poprawne X: " + next_i + " Y: " + next_j)

        return True
      sol[next_i][next_j] = -1; # backtracking

  return False

def start_knight_tour(move, x, y):
  sol = []

  for i in range(0, 8):
    a = [0]+([-1]*8)
    sol.append(a)

  x_move = [1, 2, 2, 1, -1, -2, -2, -1]
  y_move = [-2, -1, 1, 2, 2, 1, -1, -2]

  if is_valid(x, y, sol):
      sol[x][y] = 1 # placing knight at cell(1, 1)
      new_x = x + x_move[move]
      new_y = y + y_move[move]

      if is_valid(new_x, new_y, sol):
          sol[new_x][new_y] = 2
          if (knight_tour(sol, new_x, new_y, 3, x_move, y_move)):
              for i in range(0, 8):
                  print(sol[8 - i][1:])
              return True
          print("There is no solution")
          return False
      else:
          print("There is no solution")
  else:
      print("There is no solution")


i = 1
for a in range(8):
    for b in range(8):
        for c in range(8):
            print(str(i)+". SOLUTION FOR: a= "+str(a)+", b= "+str(b)+", c= "+str(c))
            i += 1
            start_knight_tour(a, b, c)