cars = ['audi', 'bmw', 'chevrolet', 'corvette', 'tesla']
for car in cars:  
    if car == 'bmw' or car == 'tesla' or car == 'audi':
        print(car.upper())
    else:
        print(car)

print("--------------------------------------------------")
# condicionales: El com dicional es el corazon de un if
# Condicional True 
car = 'bmw'
print(car == 'bmw')  # True

# Condicional False
cars_2 = 'Audi'
print(cars_2=='audi')  # False

# Condicional False
cars_2 = 'Audi'
print(cars_2.lower()=='audi')  # True

# condicional != para determinar desigualdad
requested_topping = 'mushrooms' # -> string
if requested_topping != 'anchovies': # -> True
    print("Hold the anchovies!")

    # comparadores numericos
age = 18 # ->int
print(age==18)  # True

answer = 17
if answer != 42:
    print("Esa no es la repuesta correcta. Intenta de nuevo.")

# variables numericas
age_0 = 22
age_1 = 18
print("multiplas condiciones")
print("Operacion and - pseint (Y)")
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 and age_1 >= 18)

age_0 = 22
age_1 = 18
print("multiplas condiciones")
print("Operacion or - pseint (0)")
print(age_0 >=21 or age_1 >= 21)
print(age_0 >= 23 or age_1 >= 21)

# comparadores numericos
age = 19
print(age < 21)  # True 
print(age <= 21)  # True
print(age > 21)  # False
print(age >= 21)  # False

# ¿Como preguntar si un valor esta en una lista?
print("\n A valor esta en una lista?")
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)  # True
print('pepperoni' in requested_toppings)  # False

# A value not in a list
banned_users = ["gabriel", "max", "andrik", "quevedo", "christian"]
user = "pedro"
print(user not in banned_users)  # True

# Variable de tipo BOOLEANO
game_active = True
can_edit = False


"""

if statement 

if condition:
    do something (true)

else: 
    do something (false)    

"""
print("Edad para votar")
# Preguntar la edad del usuario
# y decirle si tiene la edad 
# suficinte para votar
# input() -> siempre devuelve un string
age = int(input("Por favor ingresa tu edad: "))  # Convertir a entero
print(f"Tienes {age} años.")

if age >= 18:
    print("Tienes la edad suficiente para votar.")
else:
    print("Lo siento, no tienes la edad suficiente para votar.")    



   

