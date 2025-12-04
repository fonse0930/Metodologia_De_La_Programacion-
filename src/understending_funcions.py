## Fuciones 
# Las funciones son bloques de codigopara realizar una tarea en especifico 

# Cuando querems realizar la tarea que se a definido 
# en la funcion, tenemos que llamar el nombre de la 
# funcion que realizar la accion.

"""
   Sintaxis de funciom

   def nombre_funcion()
        acciones

Ejemplo: Vamos a definir la funcion que de un
saludo al arqui.

"""

def gretting_arqui():
    """
        Funcion para saludar a una persona 
        llamada arqui
    """
    for i in range(0,5):
        print("Hello Arqui")


gretting_arqui()
 


#Ejamplo de una funcion que genera el nombre completo de una persona o lo regrese 

def create_full_name(first_name, middle_name, last_name):
    full_name = f"{first_name.strip()} {middle_name.strip()} {last_name.strip()}".title()
    return full_name

first_name = input("dame tu primer nombre: ")
middle_name = input("dame tu segundo nombre: ") 
last_name = input("dame tu apellido:")

#Parametros psosicionales 
generated_fullname = create_full_name(
    first_name.lower(),
    middle_name.lower(),
    last_name.lower())
print(generated_fullname)    

# argumentos llave 
generated_fullname(
    middle_name = user_middle_name,
    last_name = user_last_name,
    first_name = user_first_name)