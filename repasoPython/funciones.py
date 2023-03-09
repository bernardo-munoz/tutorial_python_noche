#FUNCIONES

def miFuncion():
    print("Hola Mundo")

miFuncion()

def mostrarNombre(nombre, apellido):
    print("su nombre es: "+nombre +" " + apellido)
mostrarNombre("Bernardo", "muñoz") # Invocar la funcion

# Datos de entrada

base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura"))

# Proceso
def calcularAreaTriangulo(a,b):
    area = (base * altura)/2
    return area

# Salida
resultado = calcularAreaTriangulo (base,altura)
print("el resultado es:",resultado)

def mostrarMensaje(pais="Colombia"):
    print("Yo soy de: "+pais)

mostrarMensaje("peru")
mostrarMensaje("Ecuador")
