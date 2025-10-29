"""
 
 String variable
 En string es de manera sencilla una serie
 de caracteres. En python, todo lo que se encuentre dentro de comillas   simples (´ ´) o dobles (" ") sera conciderado un string.

 Ejempo
 "Esto es un string"
 'esto tambien es un string'
 'LE dije a un amigo "Python es mi lenguaje favorito" '
 "El lenguaje 'Python' lleva el nombre por Mobty Python,
  no por la serpiente.
"""


name = "Clase de programacion"
print(name)


# title 
print(name.title())
print(name)

""" 
Un metodo es una accion que python
puede realizar en un fracmento de datos 
o sobre una variale.

     EL punto . despues de una variable 
     seguido el metodo title() dice qu e
     si tiene que ejecutar el metodo title()
     de la variable name.

     Todos los metodos van segiuidos de parentesis
porque en ocaciones necesita informacion adicional 
para funcionar, la cual iria dentro de los parentesis.
En esta ocasion, el metodo .title() no requiere informacion
adicional para funcionar.
"""

print("Metodo upper: ", name.upper())
print("Metodo lower: ", name.lower())



# Concatenacion de STRINGS 
first_name = "alejandro"
last_name = "de_leon"
full_name = first_name + " " + last_name
print(full_name)
print(full_name.title())
