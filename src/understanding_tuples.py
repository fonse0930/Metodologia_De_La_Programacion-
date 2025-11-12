# Tuples

"""

las tuplas son listas de elementos que no cambian 
de tamaño. Las tuplas son INMUTABLES.

se utilizan los () para definirlas. 

"""

rectangle_mesaures = (200, 50) # (largo, ancho)
print(rectangle_mesaures[0])
print(rectangle_mesaures[1])

for measure in rectangle_mesaures:
    print(measure)




# regresanso a las listas 
cars = ['bwm', 'porche', 'masda']
cars_tuple = tuple(cars)
print(cars_tuple)
cars[0] = 'bmw'
cars[1] = 'porch'
cars[2] = 'mazda'
print(cars)

rectangle_mesaures = (400, 100) # (largo, ancho)
# rectangle_mesaures[0] = 500 # Error: las tuplas no pueden cambiar de tamaño
# rectangle_mesaures[1] = 200 # Error: las tuplas no pueden cambiar de tamaño
rectangle_mesaures = (300,100) # asi si se puede reasignar una tupla

"""
No podemos modificar los elementos de una tupla, pero si podemos reasignar una tupla completa.
"""