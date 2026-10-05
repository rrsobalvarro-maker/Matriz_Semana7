vector = ["j", "u", "a", "n"]
print(type(vector))  

for letra in vector:
    print(letra)
    
nombre = "Juan"
print("*"*13)
for letra in nombre:
    print(letra)
    
    
print(len(vector))
print(len(nombre))

def convertirAMayusculas(texto):
    return f"El texto {texto} en mayúsculas es {texto.upper()}"
def convertirAMinusculas(texto):
    return f"El texto {texto} en minúsculas es {texto.lower()}"
print(convertirAMayusculas(nombre))
def titulo(texto):
    return f"El texto {texto} en título es {texto.title()}"
def generarEmail(texto):
    nombre = texto.split()
    email = f"".join(palabra[:3].lower() for palabra in nombre)
    return f"{email}@uamv.edu.ni"
#print(convertirAMayusculas(vector))
for each in vector:
    print(convertirAMayusculas(each))
    
print()    
print(convertirAMinusculas(nombre))
print(convertirAMayusculas(nombre.capitalize()))
print(titulo(nombre))
print(generarEmail("Roberto Rafael Sobalvarro Gutierrez"))