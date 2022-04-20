N = int(input("Qual a ordem da matriz? "))

matr: [[int]] = [[0 for x in range(N)] for x in range(N)]

for i in range(0, N, 1):
    for j in range(0, N, 1):
        matr[i][j] = int(input(f"Elemento [{i},{j}]: "))

somaMatr = 0
for i in range(0, N, 1):
    for j in range(0, N, 1):
        if i < j:
            somaMatr = somaMatr + matr[i][j]

print(f"SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = {somaMatr}")




