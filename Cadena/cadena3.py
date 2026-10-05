#Leer una cadena de texto y buscar una palabra o texto

def buscar(valor):
  posicion = cadena.find(valor)
  if posicion >= 0:
    return "Se encontró la palabra en la posición: "
  else:
    return "No se encontró la palabra en la cadena"

cadena = input("Dime una frase: ")
valor = input("Dime la palabra que quieres buscar: ")

def saberSiContiene(cadena, valor):
    return valor in cadena

print(buscar(cadena, valor))
print(saberSiContiene(cadena, valor))