N = int(input("Qual a ordem da matriz? "))

mat: [[int]] = [[0 for x in range(N)] for x in range(N)]

for i in range(0, N, 1):
    for j in range(0, N, 1):
        mat[i][j] = int(input(f"Elemento[{i},{j}]: "))

print("MAIOR ELEMENTO DE CADA LINHA: ")
for i in range(0, N, 1):
    maior = mat[i][0]
    for j in range(0, N, 1):
        if mat[i][j] > maior:
            maior = mat[i][j]
    print(maior)




