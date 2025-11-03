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


# Whitespaces

"""
      Un whitespaces se refiere a cualquier caracter que no 
      se imprime, es decir, tabuladores y 
      finales de linea. Los whitespace se utilizan comunmente 
      para organizar las salidas de tal manera 
      que sea mas amigable de leer o ver para el usuario.

      Ejempo: 
           - Tabulador: \t
           - Salto de linea \n
"""
print("whitespace Tabulador")
print("Python")
print("\tPython")
print("\t\tPython")
print("\nPython")
print("\n\nPython")
print("\n\n")

print("Whitespace Salto de linea")
print("Lenguages: \n\tPython\nc\n\tJavascript")



# Eliminacion de espacios en blanco 
print("\nEliminacion de espacios en blanco")
Programming_lenguages = " Python "
print(Programming_lenguages.rstrip())
print(Programming_lenguages.lstrip())  
print(Programming_lenguages.strip())


# Syntax Error con string
message = 'Una fortaleza de python es su cominidad'
print(message)
message = 'Una fortaleza de python es su cominidad'
print(message)

# f-strings
famous_person = "Taylor Swift"
message = f"{famous_person} una vez dijo me voy al oxxo en avion"
print(message)

print(f"{famous_person.upper()} una vez dijo me voy al Oxxoen avion")

# Actividad 

"""
Elige el nombre de una persona famosa (quien tu quieras).
elige una cita famosa de esta persona.
iguala ambos strings a una variable.

1) Realiza la conectacion utilizando el signo de suma.
2) Realiza la conectacion utilizando fstrings.
"""

famous_person = "Moises Medina"
quote = "Una vez dijo AY! Tu marido belcast AY! tu marido belcast"
print(famous_person+" "+quote)

# Numbers

"""
    Enteros

        Los podemos sumar (+) restar (-),
        multiplicar (x) y dividir (/).
        Les podemos aplicar potencias(**2, **3, **4, ...)
        Modulo(%)

"""

number_1 = 35
number_2 = 35
suma = number_1+number_2
resta = number_1-number_2
multiplicacion = number_1*number_2
divicion = number_1/number_2
modulo = number_1%number_2

print("suma: ", suma)
print("resta: ", resta)
print("multiplicacion: ", multiplicacion)
print("divicion: ", divicion)
print("modulo:", modulo) 

print("suma: ", suma, type(suma))
print("resta: ", resta, type([resta]))
print("multiplicacion: ", multiplicacion, type(multiplicacion))
print("divicion: ", divicion, type(divicion))
print("modulo:", modulo, type(modulo)) 


"""
   Jerarquia de opeaciones 

   2+3*4 -> 14
   (2+3)*4 -> 20
   
"""

"""
      Floats
     
python llama floats a cualquier numero con punto decimal.

Los podemos sumar (+) restar (-),
        multiplicar (x) y dividir (/).
        Les podemos aplicar potencias(**2, **3, **4, ...)
        Modulo(%)

"""

print(0.1+0.1)
print(0.2-0.2)
print(0.1*2)
print(2*0.2)




# imprimir la edad de alguien 
age = 33
message = "Charly tiene " + str(age) + "años."
print(message)
"""
TypeError: Esto significa que python 
no puede reconocer el tipo de informacion 
que se esta utilizando. 

"""


