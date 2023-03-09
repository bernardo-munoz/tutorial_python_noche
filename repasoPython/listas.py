# listas

listaFrutas = ["Manzana", "banano", "Fresa", "Mango", "Melocoton"]
print("hay ",len(listaFrutas),"frutas y son: ", listaFrutas)
listaFrutas

# Tipos de datos en listas
list1 = ["Manzana", "banano", "Fresa"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1,list2, list3)

# Lista combinada
lista4 = ["abc", 34, True, 40, "xtz"]
print(lista4)

#Tuplas
#Las tuplas se utilizan para almacenar varios elementos en una sola variable.
tupla= ("Manzana", "banano", "Fresa")
print("La tupla es",tupla)

# tupla de un elemnto
tuplaUnelemnto = ("Manzana",)
print("El elemento es: ",tuplaUnelemnto)

#Tipos de datos de cadena, int y booleanos:

tupla1 = ("Manzana", "banano", "Fresa")
tupla2 = (1, 5, 7, 9, 3)
tupla3 = (True, False, False)

print("El tipo de dato es: ",type(tupla1))
print("Las tuplas son: ",tupla1,tupla2,tupla3)

#Diccionario
#Los diccionarios se utilizan para almacenar valores de datos en pares clave:valor.
#Un diccionario es una colección ordenada*, modificable y que no admite duplicados.

listaDiccionario1 = {
  "motocicleta": "yamaha",
  "modelo": "2023",
  "year": 2023
}
print(listaDiccionario1)

print(listaDiccionario1["modelo"],"es el modelo ") #Imprime el valor de "modelo" del diccionario

#Los valores duplicados sobrescribirán los valores existentes:

listaDiccionario2 = {
  "motocicleta": "yamaha",
  "modelo": "2023",
  "year": 2020,
  "year": 2023
}
print(listaDiccionario2)

print("Los elementos del diccionario son: ",len(listaDiccionario2))  #Imprime el número de elementos en el diccionario:

#Tipos de datos de cadena, int, booleanos y de lista:

listaDiccionario3 = {
  "motocicleta": "yamaha",
  "modelo": "2023",
  "year": 2020,
  "year": 2023,
  "color": ["rojo", "blanco", "Azul"]
}

print(listaDiccionario3)
print(type(listaDiccionario3)) #Imprime el tipo de datos de un diccionario: