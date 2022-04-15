M = int(input("Qual a quantidade de linhas da matriz? "))
N = int(input("Qual a quantidade de colunas da matriz? "))

matr: [[float]] = [[0 for x in range(N)] for x in range(M)]
vet: [float] = [0 for x in range(M)]

for i in range(0, M, 1):
    print(f"Digite os elementos da {i+1}a. linha:")
    for j in range(0, N, 1):
        matr[i][j] = float(input())

for i in range(0, M, 1):
    somaLinha = 0
    for j in range(0, N, 1):
        somaLinha = somaLinha + matr[i][j]
    vet[i] = somaLinha

print("VETOR GERADO:")
for i in range(0, M, 1):
    print(f"{vet[i]:.1f}")

print("finish")
