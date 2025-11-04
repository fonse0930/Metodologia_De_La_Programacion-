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