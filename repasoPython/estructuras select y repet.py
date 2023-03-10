# Estructura selectiva

a = 10
b = 15
if b > a:
  print("b es mayor que a")
else:
  print("b no es mayor que a")


a = 15
b = 10
if b > a:
  print("b es mayor que a")
elif a == b:                    # La palabra clave elif en  Python dice "si las condiciones anteriores no fueron ciertas, intente con esta condición"
  print("b es igual que a")
else:
  print("b no es mayor que a")

# si hay una sola condicion se puede usar una sola linea

if a > b: print("a es mayor que  b")

# Estructura repetitiva
# mientras i sea menor que 6 imprima i
i = 1
while i < 6:
  print(i)
  i += 1

# si i es igual a 3 pare el contador
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# si i es igual a 3 continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# Imprima un mensaje una vez que la condición sea falsa:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i llego al limite indicado que es:",i)

# Imprime cada fruta en una lista de frutas:

frutas = ["manzana", "banano", "fresa"]
for x in frutas:
  print(x)

# Repasa las letras de la palabra "banana":

for x in "banano":
  print(x)


#Salga del bucle cuando x sea "banano":

frutas = ["manzana", "banano", "fresa"]
for x in frutas:
  print(x)
  if x == "banano":
    break

#Salga del ciclo cuando xsea "banana", pero esta vez el descanso viene antes de la impresión:

frutas = ["manzana", "banano", "fresa"]
for x in frutas:
  if x == "banano":
    break
  print(x)

#No imprimir banano:

frutas = ["manzana", "banano", "fresa"]
for x in frutas:
  if x == "banano":
    continue
  print(x)

#Usando la función range():

for x in range(6):
  print(x)

#Usando el parámetro de inicio:

for x in range(2, 6):
  print(x)

#Incremente la secuencia con 3 (el valor predeterminado es 1):

for x in range(2, 30, 3):
  print(x)
  break


#Imprime todos los números del 0 al 5 e imprime un mensaje cuando el ciclo haya terminado:

for x in range(6):
  print(x)
else:
  print("final")

#Escriba cada adjetivo para cada fruta:

adj = ["red", "big", "tasty"]
fruits = ["manzana", "banano", "fresa"]

for x in adj:
  for y in fruits:
    print(x, y)

#forlos bucles no pueden estar vacíos, pero si por alguna razón tiene un forbucle sin contenido, ingrese la passdeclaración para evitar recibir un error.

for x in [0, 1, 2]:
  pass