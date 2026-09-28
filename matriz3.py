MatrizA = []

for i in range(3):
    MatrizA.append([])
    for j in range(3):
        MatrizA[i].append(float(input(f"Matriz 1--Ingrese el valor {i*3+j+1}: ")))

print("Primera matiz 3x3")
for i in MatrizA:
    print(i)

MatrizB = []

for i in range(3):
    MatrizB.append([])
    for j in range(3):
        MatrizB[i].append(float(input(f"Matriz 2--Ingrese el valor {i*3+j+1}: ")))

print("Segunda matiz 3x3")
for i in MatrizB:
    print(i)

MatrizSuma = []

for i in range(3):
    MatrizSuma.append([])
    for j in range(3):
        MatrizSuma[i].append(MatrizA[i][j] + MatrizB[i][j])

print("Suma de las dos matrices")
for i in MatrizSuma:
    print(i)