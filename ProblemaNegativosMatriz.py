
M = int(input("Qual a quantidade de linhas na matriz? "))
N = int(input("Qual a quantidade de colunas na matriz? "))

mat: [[int]] = [[0 for x in range(N)] for x in range(M)]

for i in range(0, M, 1):
    for j in range(0, N, 1):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("VALORES NEGATIVOS: ")
for i in range(0, M, 1):
    for j in range(0, N, 1):
        if mat[i][j] < 0:
            print(f"{mat[i][j]}")