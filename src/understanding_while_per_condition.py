""" 
Vamos a realizar un programa que defina un pin
para accesos de usurio 

El usuario tendra un maximo de 3 intentos


Si ususario sobrepasa este maximo de intentos
se le bloquea la cuenta.
"""

CORRECT_PIN = 123
MAX_ATTEMPTS = 3
attempt = 0 
remaining_attempts = MAX_ATTEMPTS

while attempt < MAX_ATTEMPTS:
    user_input = input("ingresa tu PIN: ")
    if user_input == CORRECT_PIN:
        prin("Acceso concedido")
        break
    else:
        attempt+=1
        remaining_attempts = MAX_ATTEMPTS - attempt
        if remaining_attempts > 0:
            print("ingresaste un pin no navido")
            print(f"te quedan{remaining_attempts}intentos")
        else: 
            print("Cuenta bloqueada.")       