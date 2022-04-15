N = int(input("Qual a ordem da matriz? "))

mat: [[int]] = [[0 for x in range(N)] for x in range(N)]

for i in range(0, N, 1):
    for j in range(0, N, 1):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("DIAGONAL PRINCIPAL:")
for i in range(0, N, 1):
    print(f"{mat[i][i]} ", end="")

print()

negativos = 0
for i in range(0, N, 1):
    for j in range(0, N, 1):
        if mat[i][j] < 0:
            negativos = negativos + 1

print(f"QUANTIDADE DE NEGATIVOS = {negativos}")
