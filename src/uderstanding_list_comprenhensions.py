"""
squares = []
for value in range(1,11):       
    square = value**2
    squares.append(square)
print("Cuadrados de los primeros 10 numeros: ", squares)

"""


"""
Una lista comprehension combina el ciclo for 
y la creacion de nuevo elemento en una sola linea 
y automaticamente agrega aun nuevo elemento a la lista.

"""

squares = [value**2 for value in range(1,11)]
print("Cuadrados de los primeros 10 numeros usando una lista comprehension: ", squares)
# para los numeros pares del 0 al 100
even_numbers = [value for value in range(0,101,2)]
print("Numeros pares del 0 al 100 usando una lista comprehension: ", even_numbers) 
# para los numeros impares del 1 al 100
odd_numbers = [value for value in range(1,101,2)]   
print("Numeros impares del 1 al 100 usando una lista comprehension: ", odd_numbers)


