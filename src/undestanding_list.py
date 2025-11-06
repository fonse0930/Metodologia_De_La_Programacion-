# Lists

"""
   Las listas nos permiten almacenar informacion 
   en un lugar, la cantidad que tenga: ya sea 
   pocos elementos o millones de elmentos.


   Se recomineda nmbrar una variable del tipo lista en plural.

   En python los corchetes [] defien una lista, sus elementos van separados por comas (,)
   Ejemplo:


"""
bicycles=['trek', 'canondale', 'redline', 'specialized', 'giant']
print(bicycles)

print(bicycles[0].title())


# Los indices comienzan en 0 y terminan en n-1, donde n es el numero de elementos 
print(bicycles[4].title())

# Accediendo al ultimo elemento 
print(bicycles[-1].title()) # Ultimo elemento 
print(bicycles[-2].title()) # Penultimo elemento
print(bicycles[-5].title()) # Primer elemento 
  
# Utilizando valores de la lista 
message = "Mi primer bicivleta fue una " + bicycles[4].title() +"."
print(message)

message_f = f"Mi primer bicicleta fue una {bicycles[4].title()}:"
print(message_f)

## Agrgar elementos a una lista 
print("\n")
print("Agregar elementos a una lista.")
print(bicycles)

print("MEtodo de la lista patra agregar elementos: list_name.append(element)")
bicycles.append("ducati")
print(bicycles)
"""
# Lista A-105
    Agrega ele,mentois al final de una lista 
     - append(): Agrega un elemento al final de la lista


"""
print("\n--- Agregar elementos a lista metodo append()---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # SSalida: ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles) # Salida: ['honda', 'yamaha', suzuki', ducati']



"""
    
    Agregar elementos en una pocison espesifica 
    - insert(): Inserta un elemengto en una pocision espesifica 

"""

print("\n--- Agregar elementos a lista metodo append()---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # SSalida: ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1, 'ducati'),
print(motorcycles) # Salida: ['honda', 'ducati', 'yamaha', suzuki']

"""
-pop() Elimina y devuelve el ultimo elemento de la lista 

"""
print("\n--- Eliminar elementos de una lista metodo pop()---")
motorcycles = ['honda', 'yamaha', 'suzuki']                             
print(motorcycles) # SSalida: ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles) # Salida: ['honda', 'yamaha']
print(popped_motorcycle) # Salida: suzuki   
print("\n--- Eliminar elementos de una lista metodo remove()---")





"""
Ejemplo;
"""     



 
students = ["alejandro", "luis", "max", "santiago", "gabriel"]
print(students)
desired_student = input("¿que estudiante quieres retirar de la lista?")
students.remove(desired_student.strip().lower())
print(students)
print("Tu has eliminado a " + desired_student.title() + " de la lista de estudiantes.")
students.reverse()
print(students)

print(len(students))

print(sorted(students))
print(students)

cars = ["kia", "ford", "chevrolet", "audi", "bmw"]
print(cars)
print(sorted(cars))
sorted_list = sorted(cars)
print("lista original:", cars)