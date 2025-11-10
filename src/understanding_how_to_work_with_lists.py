

"""
 recorrer una lista sin importar la cantidad
 de elemetnos que tenga
"""
magicians = ["ron","hermione","harry"]

print(magicians[0],magicians[1],magicians[2])

for magician in magicians :
   print(magician)
   print(magician.upper())
   print(f"{magician.title()} eso fue un gran hechizo")
   print(f"\t {magician.lower()} no podemos esperar a ver el siguiente hechizo")

print("Gracias a todos por participar en el show")
"""
python utiliza la indentacion para definir bloques de codigo
 en lugar de llaves {} o palabras clave como begin end
"""





""" 
Python utiliza la identificacion para determinar la estructura del codigo
Se recomienda nombrar una variable del tipo lista en plural.    
basicamente se utilizan cuatro lineas de codigo para trabajar con listas en python:
- Crear una lista   
- Acceder a los elementos de una lista
- Agregar elementos a una lista
- Eliminar elementos de una lista

"""



# Error de logica  
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
print(f"I can´t wait to see your next trick, {magician.title()}.\n")

# Identacion inecesaria
messages = "Hola python"


