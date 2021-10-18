def print_matrix(M):
  for r in M:
    print(r)

sign = lambda a: (a>0) - (a<0) #-1 if negative, 1 if positive

X = [[-10, 0, 9, 0],
     [0, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 2]]

Y = [[10, 0, -9, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 8]]   

Z = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]  
print(Z)

for i in range(len(Z)):
  for j in range(len(Z[0])):
    Z[i][j] = abs(X[i][j]) + abs(Y[i][j])
    if sign(X[i][j]) != sign(Y[i][j]):
      Z[i][j] *= -1

print_matrix(Z)