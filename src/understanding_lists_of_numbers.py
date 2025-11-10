""" 
Las listas tambien pueden almacenar 
numeros y de echos, son ideales para esto.
Python ofrece una gran cantidad de herraminentas que nos aydudan a tranajar.


"""

# Metodo bult in name 


"""
ejemplo:

"""
print("Numeros del 0 al 9")
for value in range(10): # 10 numeros entre 0-9
    print(value)

print("Numeros del 1 al 9")
for value in range(1,10): # 10 numeros entre 1-9
    print(value)
for value in range(1,21): # 20 numeros entre 1-20
    print(value)

print("Numeros impares del 1 al 9")
for value in range(1,10,2): # 10 numeros entre 1-
    print(value)
numeros_pares = list(range(0,10,2))
print(numeros_pares)        

print("Numeros pares del 0 al 9")
for value in range(0,10,2): # 10 numeros entre 0-9
    print(value)
numeros_pares = list(range(0,10,2))
print(numeros_pares)

print("tabla del 8")
for value in range(0,81,8): # 10 numeros entre 1-9
    print(value)
tabla_del_8 = list(range(0,81,8))
print(tabla_del_8)  


# Cuadrado de los porimeros 10 numeros 
cuadrados = []
for value in range(1,11):
    cuadrado = value**2
    cuadrados.append(cuadrado)
print("Cuadrados de los primeros 10 numeros: ", cuadrados)


# Cubo de los primeros 10 numeros
cubos = []      
for value in range(1,11):
    cubo = value**3
    cubos.append(cubo)
print("Cubos de los primeros 10 numeros: ", cubos)

# Mas metodos bult in para trabajar con listas de numeros
# Metodo min()
digisitos = [1,2,3,4,5,6,7,8,9,0]
print(min(digisitos)) # Salida: 0
print(max(digisitos)) # Salida: 9           
print(sum(digisitos)) # Salida: 45
# Metodo sum()
print(sum(digisitos)) # Salida: 45
# Metodo len()
print(len(digisitos)) # Salida: 10
# Metodo sorted()
print(sorted(digisitos)) # Salida: [0,1,2,3,4,5,6,7,8,9]