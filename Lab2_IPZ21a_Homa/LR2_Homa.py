def print_matrix(M):
  for r in M:
    print(r)

Z = [[0, 1, 2, 3, 4, 5],
     [6, 0, 1, 2, 3, 4],
     [7, 5, 0, 1, 2, 3],
     [8, 6, 7, 0, 1, 2],
     [9, 7, 8, 9, 0, 1],
     [0, 8, 7, 9, 6, 0]]
print_matrix(Z)
print("\n")

result = [[Z[j][i] for j in range(len(Z))] for i in range(len(Z[0]))]

print_matrix(result)
print("\n")