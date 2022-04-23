import math

N = int(input("Qual a ordem da matriz? "))

matr: [[int]] = [[0 for x in range(N)] for x in range(N)]

soma = 0
for i in range(0, N, 1):
    for j in range(0, N, 1):
        matr[i][j] = float(input(f"Element [{i},{j}]: "))
        if matr[i][j] > 0:
            soma = soma + matr[i][j]

print(f"\nSOMA DOS POSITIVOS: {soma:.1f}\n")

indlinha = int(input("Escolha uma linha: "))

print("LINHA ESCOLHIDA: ", end="");

for i in range(0, N, 1):
    print(f"{matr[indlinha][i]:.1f} ", end="")

indlinha = int(input("\n\nEscolha uma coluna: "))

print("COLUNA ESCOLHIDA: ", end="");

for i in range(0, N, 1):
	print(f"{matr[i][indlinha]:.1f} ", end="")

print("\n\nDIAGONAL PRINCIPAL: ", end="");

for i in range(0, N, 1):
	print(f"{matr[i][i]:.1f} ", end="")

for i in range(0, N, 1):
	for j in range(0, N, 1):
		if matr[i][j] < 0:
			matr[i][j] = math.pow(matr[i][j], 2);

print("\n\nMATRIZ ALTERADA:");

for i in range(0, N, 1):
	for j in range(0, N, 1):
		print(f"{matr[i][j]:.1f} ", end="")
	print()