""" 
slicing a list 

"""
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Lista original:", players)

print("Slice de lista original", players[0:3])    
print("Slice de lista original", players[1:4])  
print("Slice de lista original", players[:4]) 
print("Slice de lista original", players[2:])
print("Slice de lista original", players[-3:])
print("Slice de lista original", players[5:2])
print("Slice de lista original", players[-3:-1])


"""
      slicing en un ford 
"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Aqui se representan los tres primeros jugadores del equipo")
for players in players[0:3]
    print(player.title() )

"""
copiando listas
"""
my_foods = ['pizza', 'tacos', 'flautas', 'gordityas']
# my_foods_copy =my_foods # Error: esta no es la manera correcta de copiar una lista 
my_foods_1 = my_foods[:]
my_foods_2 = my_foods.copy()
my_foods_3 = list(my foods)