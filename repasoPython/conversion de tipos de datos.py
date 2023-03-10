x = 1 # int
y = 2.8 # float
z = 1j # complex

#convierte desde entero a float:
a = float(x)

#convierte desde float a entero:
b = int(y)

#convierte desde entero a complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Convierte entero a float
f = 57
print(float(f))

# de float a entero
b = 125.0
c = 390.8

print(int(b))
print(int(c))

# en division de obtiene flotante
a = 5 / 2
print(a)

# entero a cadena

# convertimos el entero a caddena
user = "Sammy"
lines = 50

print("felicdades, " + user + "! acabas de escribir " + str(lines) + " lineas de codigo.")


#Cuando colocamos un flotante en el método str(), se mostrará un valor de cadena del flotante
print(str(421.034))
f = 5524.53
print(str(f))

#el método int() que convertirá las cadenas en enteros,
#lo que nos permitirá realizar cálculos matemáticos con valores que eran originalmente cadenas.
linasAyer= "50"
lineasHoy = "108"

lineasTotal = int(linasAyer) - int(lineasHoy)
print(lineasTotal)

#convierte lista en tupla
print(tuple(['mazana', 'pera', 'mago', 'papaya']))

# lista a tupla en letras
print(tuple('Sammy'))

#convertios tupla a lista
print(list(('mazana', 'pera', 'mago', 'papaya')))

# las cadenas las podemos convertir en lisitas
print(list('mago'))