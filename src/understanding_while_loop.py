# While

"""
El whil es un ciclo controlado/comandado 
por condicion.

La estructura basicas de whil es:

    while conditional:
        action

"""
# While infinito
"""
Programa si el usuario escribe un numero
entre en 25 y el 50 entonces esta dentro del 
rango y salirme de while, 
de otro modo pedirle el numero.

"""
while True:
    try:
        number = int(input("Ingresa tu numero: "))

        if number >= 25 and number <= 50: 
            print("Estas en el rango, lo isite bien")
        else:
            print("Estas fuera del rango, intentalo otra vez")
    except:
        print("Introdusiste una variable no valida")