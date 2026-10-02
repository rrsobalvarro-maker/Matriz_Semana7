from colorama import fore, Style

n = int(input("Ingrese el tamaño de la matriz cuadrada: "))
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

print("La matriz identidad es: ")
for fila in matriz:
    print(fila)

for i in range(n):
    for j in range(n):
        if i == j:
            print(fore.Blue + str(matriz[i][j]) + Style.RESET_ALL, end =" ")
        else:
            print(matriz[n][j], end=" ")
    print()