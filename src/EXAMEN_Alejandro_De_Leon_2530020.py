
# Problema 1

def suma_numeros(n):
    suma_total = sum(range(1, n + 1))
    suma_pares = sum(i for i in range(1, n + 1) if i % 2 == 0)
    suma_impares = sum(i for i in range(1, n + 1) if i % 2 != 0)
    return suma_total, suma_pares, suma_impares
n = int(input("Ingrese un numero entero positivo n: "))
suma_total, suma_pares, suma_impares = suma_numeros(n)
print(f"Suma total desde 1 hasta {n}: {suma_total}")
print(f"Suma de numeros pares desde 1 hasta {n}: {suma_pares
}")
print(f"Suma de numeros impares desde 1 hasta {n}: {suma_impares}")





# RESCATE
""" 
fibunacci

"""

def fibonacci(n):   
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
n = int(input("Ingrese la posicion n para obtener el numero: "))
print(f"El numero de Fibonacci en la posicion {n} es: {fibonacci(n)}")




# las otra de respuesta 
"""
bonito es mejor que feo
"""

