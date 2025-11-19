

"""
    Hacer un programa que pregunte la edad de una persona 
    y responda lo siguiente 

       - si la edad es menor o igual a 4, entoses la etrada 
       es gratuita.
       - Si la edad es menor a 18, pero mayor a 4 
       entonses la entrada cuesta $280
       - Si la edad es mayor o igual a 18, entonses la entrada cuesta $400

       """

try: 
    age = int(input("escribe tuedad: ")) 
except: 
    age = -1
    print("Error, ingresaste un caracter no valido")    





if age <= 4 and age >= 0:
    print("Entrada gratuita")

elif age < 18 and age > 4:
    print("La entrada cuesta $200.")

elif age >= 18: 
    print("La entrada cuesta $400.")

else:
    print("Tuviste un error")    


# Utilizando varias listas 

guisos_disponibles = ['salsa verde', 'desebrada', 'mole']
guisos_a_ordenar = ['desebrada', 'caldo de iguanas']

print("¿Que guiso desea ordenar?")
for guiso in guisos_a_ordenar:
    print(f"Deseo {guiso}")
    if guiso in guisos_disponibles:
        print(f"Si tenemos {guiso}")
    else:
        print(f"Lo siento, no tenemos {guiso} disponible")
print("Realiza tu pedido...")        