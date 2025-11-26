"""
 for understanding_while_loop_centinel

un programa que:
    - Cuente cuantos numero ha infresado el usuario 
    - Realize la suma de estos numeros 
    - Me diga cual es el numero minimo de los numeros inf¿gresados 
    - Me diga cual es el maximo de los nmeros ingresados 

"""
counte = 0
sum_quantities = 0.0
minimum = None 
maximum = None 

while True:
    print("Escribe exit para salir")
    user_input = input("Ingresa una conatdidad (MXN): ")
    
    if user_input == exit :
        break

    try: 
        value = float(user_input)
    except ValueError:
        print("Caracter invalido. Por favor ingrese un numero")
    except KeyboardInterrupt: 
        print("salida manual")
        break

    counter+=1   # counter = counter + 1
    sum_quantities += value    # sum_quantities = sum_quantities + value                     

    
    if minimum is None or value < minimum:
        minimum = value

    if minimum is None or value > minimum:
        minimum = value    
    


print("cantidad de numeros ingresados: ", counter)
print("suma de cantidades: ", sum_quantities)
print("minimum de cantidades:", minimum)
print("maximum de cantidades:", maximum)    

