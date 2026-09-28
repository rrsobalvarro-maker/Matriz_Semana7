matriz = []

for i in range(2):
    matriz.append([])
    for j in range(2):
        matriz[i].append(int(input(f"Ingrese el valor: ")))

print("La matriz 2x2 es: ")
for i in matriz:
    print(i)