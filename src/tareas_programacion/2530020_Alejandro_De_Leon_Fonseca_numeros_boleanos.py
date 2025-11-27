# ALEJANDRO DE LEON FONSECA
# 2530020
# NUMEROS BOOLEANOS


"""Los números booleanos son una parte fundamental de la lógica computacional y
la programación. Representan dos estados posibles: verdadero (True) y falso (False),
lo que los convierte en herramientas esenciales para la toma de decisiones y el control
de flujo en los programas. En Python, los valores booleanos se representan con las
palabras clave True y False, y se utilizan en diversas operaciones lógicas y condicionales.
Los números booleanos se derivan de la lógica binaria, donde 1 representa verdadero y
0 representa falso. Esta dualidad permite a los programadores evaluar condiciones,
realizar comparaciones y controlar la ejecución de bloques de código en función de
diferentes criterios. Por ejemplo, en estructuras condicionales como if, los valores
booleanos determinan qué camino tomará el programa según si una condición es verdadera
o falsa.
Además, los números booleanos son fundamentales en operaciones lógicas como AND,
OR y NOT, que permiten combinar múltiples condiciones para crear expresiones más
complejas. Estas operaciones son cruciales en la toma de decisiones dentro de los programas,
ya que permiten evaluar múltiples criterios simultáneamente.
En resumen, los números booleanos son una herramienta esencial en la programación,
permitiendo a los desarrolladores implementar lógica y control de flujo de manera efectiva.

Los tipos int y float en Python representan números enteros y números con decimales, respectivamente,
y se diferencian en que los int no tienen parte fraccionaria mientras que los float permiten mayor
precisión numérica. Un booleano es un valor lógico (True o False) que normalmente se obtiene al realizar
comparaciones como ==, >, < o >=, y sirve para tomar decisiones dentro del programa. Validar rangos es
importante para evitar cálculos incorrectos y la división entre cero debe prevenirse porque genera errores
que detienen la ejecución del código. Este documento analizará cada problema definiendo las entradas y
salidas esperadas, las validaciones necesarias y el uso de enteros, flotantes y booleanos para controlar
el flujo del programa y asegurar que los resultados sean confiables y seguros.


"""
## PRINCIPIOS Y BUENA PRACTICA DE ELLOS 
"""
 Sobre los valores booleanos:
- En Python, un booleano (bool) es un tipo de dato que solo puede tomar dos valores: True o False,
los cuales representan decisiones lógicas dentro del programa.
- Los booleanos suelen obtenerse mediante comparaciones, como x > 0, x == y o x <= límite,
y permiten controlar el flujo del programa mediante condiciones y validaciones.
- Es importante interpretar correctamente qué significa que una expresión sea True o False: por ejemplo,
True puede indicar que un dato es válido, que un rango es correcto o que una operación puede ejecutarse,
mientras que False puede señalar errores, valores no permitidos o situaciones que deben corregirse.
- Comprender los booleanos es esencial para diseñar validaciones sólidas, evitar fallos en cálculos
numéricos y asegurar que los programas tomen decisiones correctas según la lógica establecida.

"""

# PROBLEMA 1
## Temperature converter and range flag

# === Temperature Converter and Range Flag ===

def convert_temperature(temp_c_str):
    # Validación: intentar convertir a float
    try:
        temp_c = float(temp_c_str)
    except ValueError:
        return "Error: la temperatura debe ser un número."

    # Conversión a Kelvin
    temp_k = temp_c + 273.15

    # Validación física: Kelvin no puede ser negativo
    if temp_k < 0:
        return "Error: la temperatura ingresada es físicamente imposible (Kelvin < 0)."

    # Conversión a Fahrenheit
    temp_f = temp_c * 9 / 5 + 32

    # Booleano según rango
    is_high_temperature = (temp_c >= 30.0)

    # Salida final
    resultado = (
        f"Fahrenheit: {temp_f}\n"
        f"Kelvin: {temp_k}\n"
        f"High temperature: {is_high_temperature}"
    )

    return resultado


# Programa principal
print("=== Temperature Converter ===")
user_input = input("Ingresa la temperatura en °C: ")

print("\n" + convert_temperature(user_input))


input("\nPresiona ENTER para salir...")

# PROBLEMA 2
## Work hours and overtime payment
# === Work Hours and Overtime Payment ===
def calculate_payment(hours_str, rate_str):
    # Validación: intentar convertir a float
    try:
        hours = float(hours_str)
        rate = float(rate_str)
    except ValueError:
        return "Error: las horas y la tarifa deben ser números."

    # Validación de horas y tarifa no negativas
    if hours < 0 or rate < 0:
        return "Error: las horas y la tarifa no pueden ser negativas."

    # Cálculo del pago
    if hours <= 40:
        total_payment = hours * rate
    else:
        overtime_hours = hours - 40
        total_payment = (40 * rate) + (overtime_hours * rate * 1.5)

    return f"Total payment: ${total_payment:.2f}"
# Programa principal
print("=== Work Hours and Overtime Payment ===")
user_hours = input("Ingresa las horas trabajadas: ")
user_rate = input("Ingresa la tarifa por hora: ")
print("\n" + calculate_payment(user_hours, user_rate))

input("\nPresiona ENTER para salir...")


# PROBLEMA 3
## Discount eligibility with booleans

def discount_eligibility():
    print("=== Discount Eligibility Checker ===")

    # Entrada del total
    total_text = input("Total de la compra: ")

    # Validación del total
    try:
        purchase_total = float(total_text)
    except ValueError:
        print("Error: el total debe ser un número válido.")
        return

    if purchase_total < 0.0:
        print("Error: el total no puede ser negativo.")
        return

    # Entrada y normalización de textos
    is_student_text = input("¿Es estudiante? (YES/NO): ").strip().upper()
    is_senior_text = input("¿Es adulto mayor? (YES/NO): ").strip().upper()

    # Validación de texto
    valid_inputs = ["YES", "NO"]
    if is_student_text not in valid_inputs or is_senior_text not in valid_inputs:
        print("Error: invalid input (solo se acepta YES o NO).")
        return

    # Conversión a booleanos
    is_student = (is_student_text == "YES")
    is_senior = (is_senior_text == "YES")

    # Lógica del descuento
    discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)

    # Cálculo final
    if discount_eligible:
        final_total = purchase_total * 0.90
    else:
        final_total = purchase_total

    # Salidas
    print("\nResultados:")
    print("Discount eligible:", str(discount_eligible).lower())
    print("Final total:", final_total)

# Ejecutar
discount_eligibility()
input("\nPresiona ENTER para salir...")

# PROBLEMA 4
##  Basic statistics of three integers
print("=== Basic Statistics ===")

# Entradas
n1_input = input("Ingresa n1: ")
n2_input = input("Ingresa n2: ")
n3_input = input("Ingresa n3: ")

# Validación de enteros
try:
    n1 = int(n1_input)
    n2 = int(n2_input)
    n3 = int(n3_input)
except ValueError:
    print("Error: los tres valores deben ser enteros.")
    input("\nPresiona ENTER para salir...")
    exit()

# Cálculos
sum_value = n1 + n2 + n3
average_value = sum_value / 3
max_value = max(n1, n2, n3)
min_value = min(n1, n2, n3)
all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

# Resultados
print("\nSum:", sum_value)
print("Average:", average_value)
print("Max:", max_value)
print("Min:", min_value)
print("All even:", all_even)

input("\nPresiona ENTER para salir...")

# PROBLEMA 5
## Loan eligibility (income and debt ratio)
print("=== Loan Eligibility ===")

income_text = input("Enter monthly income: ")
debt_text = input("Enter monthly debt: ")
credit_text = input("Enter credit score: ")

# Validaciones
try:
    monthly_income = float(income_text)
    monthly_debt = float(debt_text)
    credit_score = int(credit_text)

    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
        input("\nPress ENTER to exit...")
        exit()

except:
    print("Error: invalid input")
    input("\nPress ENTER to exit...")
    exit()

# Calcular relación deuda/ingreso
debt_ratio = monthly_debt / monthly_income

# Regla de elegibilidad
eligible = (
    monthly_income >= 8000.0 and
    debt_ratio <= 0.4 and
    credit_score >= 650
)

print("Debt ratio:", debt_ratio)
print("Eligible:", str(eligible).lower())

input("\nPress ENTER to exit...")

#PROBLEMA 6
##Body Mass Index (BMI) and category flag
print("=== BMI Calculator ===")

weight_text = input("Peso (kg): ")
height_text = input("Estatura (m): ")

# Validaciones
try:
    weight_kg = float(weight_text)
    height_m = float(height_text)
except:
    print("Error: invalid input")
    exit()

if weight_kg <= 0.0 or height_m <= 0.0:
    print("Error: invalid input")
    exit()

# Cálculo de BMI
bmi = weight_kg / (height_m * height_m)
bmi_rounded = round(bmi, 2)

# Booleanos
is_underweight = (bmi < 18.5)
is_normal = (18.5 <= bmi < 25.0)
is_overweight = (bmi >= 25.0)

print("BMI:", bmi_rounded)
print("Underweight:", str(is_underweight).lower())
print("Normal:", str(is_normal).lower())
print("Overweight:", str(is_overweight).lower())

"""
Los distintos programas permitieron comprender cómo los tipos numéricos (int y float) y los 
valores booleanos trabajan juntos para realizar cálculos, evaluaciones lógicas y validaciones 
confiables. A través de estos ejercicios se reforzó la importancia de convertir correctamente 
las entradas del usuario, verificar rangos válidos y evitar errores comunes como divisiones 
entre cero o valores físicamente imposibles. También se evidenció que los booleanos 
son fundamentales para tomar decisiones automáticas, como determinar si una temperatura 
es alta, si un cliente recibe descuento, si alguien es elegible para un préstamo o si 
su BMI se encuentra dentro de un rango saludable. Además, el uso de operaciones matemáticas 
básicas, comparaciones y funciones incorporadas como max(), min() y round() permitió 
producir resultados precisos y claros para el usuario. En general, 
estos programas demostraron cómo un diseño correcto de validaciones y estructuras 
lógicas mejora la confiabilidad y seguridad del código, permitiendo procesar datos numéricos 
de forma profesional y estructurada.
"""
# References:
"""
1) Python Documentation Built-in Types: Numeric Types (int, float).
https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

2) Python Documentation Boolean Operations and Comparisons.
https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not

3) "Automate the Boring Stuff with Python" Al Sweigart.
Capítulos sobre manejo de números, validaciones y entradas de usuario.

4) "Think Python: How to Think Like a Computer Scientist" Allen B. Downey.
Secciones sobre expresiones booleanas, decisiones y manejo de errores.

5) Real Python Tutorial: “Python Numbers, Booleans, and Input Validation”.
https://realpython.com/python-data-types/
"""