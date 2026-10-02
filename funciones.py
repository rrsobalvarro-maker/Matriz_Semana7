def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)


# 1. Multiplicar una matriz por un escalar
def escalar_matriz(matriz, k):
    matrizB = []

    for i in range(len(matriz)):
        matrizB.append([])

        for j in range(len(matriz[i])):
            matrizB[i].append(k * matriz[i][j])

    return matrizB


# 2. Crear una matriz 2x2
def crear_matriz():
    matriz = []

    for i in range(2):
        matriz.append([])

        for j in range(2):
            valor = int(input(
                f"Digite el valor de la posición [{i}][{j}]: "
            ))
            matriz[i].append(valor)

    return matriz


# Crear una matriz 3x3
def crear_matriz_3x3():
    matriz = []

    for i in range(3):
        matriz.append([])

        for j in range(3):
            valor = int(input(
                f"Digite el valor de la posición [{i}][{j}]: "
            ))
            matriz[i].append(valor)

    return matriz


# 3. Suma de matrices
def sumar_matrices(matriz1, matriz2):
    matriz_resultado = []

    for i in range(3):
        matriz_resultado.append([])

        for j in range(3):
            matriz_resultado[i].append(
                matriz1[i][j] + matriz2[i][j]
            )

    return matriz_resultado


# 4. Multiplicación de matrices 2x2
def multiplicar_matrices(matrizA, matrizB):
    matrizC = []

    for i in range(2):
        fila = []
        matrizC.append(fila)

        for j in range(2):
            suma = 0

            for k in range(2):
                suma += matrizA[i][k] * matrizB[k][j]

            matrizC[i].append(suma)

    return matrizC


# 5. Matriz identidad
def matriz_identidad(n):
    matriz = []

    for i in range(n):
        fila = []

        for j in range(n):
            if i == j:
                fila.append(1)
            else:
                fila.append(0)

        matriz.append(fila)

    return matriz