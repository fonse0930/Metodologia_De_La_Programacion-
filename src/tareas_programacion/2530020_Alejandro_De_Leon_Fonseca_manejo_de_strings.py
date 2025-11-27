# ALEJANDRO DE LEON FONSECA                                      #2530020
                                # MANEJO DE STRINGS



"""
El manejo de strings en Python constituye uno de los pilares
fundamentales del lenguaje, debido a que gran parte de los datos 
procesados en programas modernos se representa en forma de texto.
Python ofrece un sistema de cadenas robusto, flexible y altamente
intuitivo, basado en objetos inmutables. Esto significa que, 
cada vez que se modifica una cadena, Python genera una nueva, lo cual 
favorece la seguridad y la consistencia en el manejo de datos.

El lenguaje proporciona una amplia variedad de métodos integrados para 
manipular strings, permitiendo realizar operaciones como convertir 
mayúsculas y minúsculas, buscar patrones, dividir y unir texto, 
eliminar espacios innecesarios y validar contenido. 
Estas herramientas facilitan un desarrollo más eficiente y reducen la 
necesidad de implementar funciones manuales complejas.

Python también ofrece soporte completo para Unicode, lo cual permite 
trabajar con caracteres de prácticamente cualquier idioma incluyendo 
acentos, emojis y símbolos especiales— sin dificultades. 
Asimismo, el uso de f-strings, incorporado a partir de la versión 3.6, 
simplifica notablemente la construcción de cadenas dinámicas y mejora 
la legibilidad del código.

Por su parte, las técnicas de indexación y slicing posibilitan acceder 
a secciones específicas de una cadena de forma precisa y rápida, 
mientras que la librería estándar y módulos adicionales proporcionan 
herramientas avanzadas para tareas como expresiones regulares, 
análisis de texto y procesamiento de datos estructurados.

En conjunto, el manejo de strings en Python combina simplicidad 
sintáctica, capacidad expresiva y herramientas avanzadas, 
lo que convierte al lenguaje en una opción muy poderosa para 
aplicaciones que requieren manipulación intensiva de información 
textual, como análisis de datos, automatización, 
desarrollo web y ciencia de datos.

"""
# PROBLEM 1
## Full name formatter (name + initials) usando strings
def format_full_name(full_name):
    # 1. Normalizar el texto
    clean_name = full_name.strip()

    # Validación: nombre vacío
    if not clean_name:
        return "Error: el nombre no puede estar vacío."

    # Separar en palabras
    parts = clean_name.split()

    # Validación: mínimo dos palabras
    if len(parts) < 2:
        return "Error: el nombre debe contener al menos dos palabras."

    # 2. Formatear en Title Case
    formatted_name = " ".join(parts).title()

    # 3. Generar iniciales
    initials = ""
    for word in parts:
        initials += word[0].upper() + "."

    # 4. Resultado final
    return f"Formatted name: {formatted_name}\nInitials: {initials}"


print("=== Full Name Formatter ===")
user_input = input("Escribe tu nombre completo: ")

resultado = format_full_name(user_input)
print("\n" + resultado)

# Pausa para que PowerShell no cierre la ventana (opcional)
input("\nPresiona ENTER para salir...")

# PROBLEMA 2
## simple email validator usando strings
def validate_email(email):
    # 1. Normalizar el texto
    clean_email = email.strip()

    # Validación: email vacío
    if not clean_email:
        return "Error: el correo electrónico no puede estar vacío."

    # 2. Validar formato básico
    if "@" not in clean_email or "." not in clean_email.split("@")[-1]:
        return "Error: formato de correo electrónico inválido."

    # 3. Validar caracteres no permitidos
    invalid_chars = set(" ,;:/\\[]{}()<>")
    if any(char in invalid_chars for char in clean_email):
        return "Error: el correo electrónico contiene caracteres no permitidos."

 
    return f"Correo electrónico válido: {clean_email}"

print("=== Simple Email Validator ===")
user_email = input("Escribe tu correo electrónico: ")
resultado_email = validate_email(user_email)
print("\n" + resultado_email)

input("\nPresiona ENTER para salir...")

# PROBLEMA 3
## Palindrome checker (ignoring spaces and case)
def is_palindrome(phrase):
    # 1. Normalizar el texto
    clean_phrase = phrase.replace(" ", "").lower()

    # Validación: frase vacía
    if not clean_phrase:
        return "Error: la frase no puede estar vacía."

    # 2. Verificar si es palíndromo
    reversed_phrase = clean_phrase[::-1]
    if clean_phrase == reversed_phrase:
        return f'"{phrase}" es un palíndromo.'
    else:
        return f'"{phrase}" no es un palíndromo.'
print("=== Palindrome Checker ===")
user_phrase = input("Escribe una frase: ")
resultado_palindrome = is_palindrome(user_phrase)
print("\n" + resultado_palindrome)

input("\nPresiona ENTER para salir...")

# PROBLEMA 4
## Sentence word stats (lengths and first/last word)
def sentence_word_stats(sentence):
    # 1. Normalizar el texto
    clean_sentence = sentence.strip()

    # Validación: oración vacía
    if not clean_sentence:
        return "Error: la oración no puede estar vacía."

    # 2. Dividir en palabras
    words = clean_sentence.split()

    # Validación: al menos una palabra
    if len(words) == 0:
        return "Error: la oración debe contener al menos una palabra."

    # 3. Calcular estadísticas
    word_lengths = [len(word) for word in words]
    first_word = words[0]
    last_word = words[-1]

    # 4. Resultado final
    stats = {
        "total_words": len(words),
        "word_lengths": word_lengths,
        "first_word": first_word,
        "last_word": last_word
    }
    return stats
print("=== Sentence Word Stats ===")
user_sentence = input("Escribe una oración: ")
resultado_stats = sentence_word_stats(user_sentence)
print("\nEstadísticas de la oración:")
for key, value in resultado_stats.items():
    print(f"{key}: {value}")
input("\nPresiona ENTER para salir...")


# PROBLEMA 5
##  Password strength classifier
def classify_password_strength(password):
    # 1. Normalizar el texto
    clean_password = password.strip()

    # Validación: contraseña vacía
    if not clean_password:
        return "Error: la contraseña no puede estar vacía."

    # 2. Evaluar fuerza de la contraseña
    length = len(clean_password)
    has_upper = any(c.isupper() for c in clean_password)
    has_lower = any(c.islower() for c in clean_password)
    has_digit = any(c.isdigit() for c in clean_password)
    has_special = any(not c.isalnum() for c in clean_password)

    strength = "Débil"
    if length >= 8 and has_upper and has_lower and has_digit and has_special:
        strength = "Fuerte"
    elif length >= 6 and (has_upper or has_lower) and has_digit:
        strength = "Moderada"

    return f"La fuerza de la contraseña es: {strength}"
print("=== Password Strength Classifier ===")
user_password = input("Escribe una contraseña: ")
resultado_password = classify_password_strength(user_password)
print("\n" + resultado_password)
input("\nPresiona ENTER para salir...")

# PROBLEMA 6
## Product label formatter (fixed-width text)
def format_product_label(product_name, price):
    # 1. Normalizar el texto
    clean_name = product_name.strip().title()
    clean_price = f"${price:.2f}"

    # 2. Formatear etiqueta
    label_width = 30
    name_part = clean_name.ljust(label_width - len(clean_price))
    label = f"{name_part}{clean_price}"

    return label
print("=== Product Label Formatter ===")
user_product = input("Escribe el nombre del producto: ")
user_price = float(input("Escribe el precio del producto: "))
resultado_label = format_product_label(user_product, user_price)
print("\nEtiqueta del producto:")
print(resultado_label)
input("\nPresiona ENTER para salir...")
 
"""
 El manejo de strings es fundamental porque casi toda la información que ingresa o sale de un programa
 se expresa como texto, por lo que saber limpiarlo, transformarlo y validarlo evita errores. Métodos como
 lower(), strip(), split() y join() son útiles para normalizar el texto: eliminar espacios sobrantes,
 unificar mayúsculas/minúsculas y reorganizar palabras según se necesite. Normalizar antes de comparar es
 importante porque dos textos pueden parecer distintos visualmente, pero ser iguales si se quitan espacios
 o se uniforma su formato. También aprendí que las validaciones evitan datos basura y aseguran que el
 programa funcione incluso cuando la entrada del usuario es incorrecta. Finalmente, comprendí que los
 strings son inmutables, por lo que cada transformación crea una nueva cadena, y que los slices permiten
 extraer o invertir texto de forma eficiente sin modificar el original.
"""

# REFERENCIAS 
""" 
 1) Python Documentation Built-in Types: Text Sequence Type — str.
    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

 2) Python Documentation  String Methods.
    https://docs.python.org/3/library/stdtypes.html#string-methods

 3) "Automate the Boring Stuff with Python"  Al Sweigart.
    Capítulos sobre manejo de texto, validación de datos y expresiones regulares.

 4) "Think Python: How to Think Like a Computer Scientist"  Allen B. Downey.
    Sección sobre cadenas, inmutabilidad y slicing.

 5) Real Python  Tutoriales sobre manejo de strings y buenas prácticas de input.
    https://realpython.com/python-strings/

 6) Artículo: “Best Practices for User Input Validation in Software Development.”
    IEEE Software Engineering Notes.

 7) Apuntes de Algoritmos y Programación Básica  Manejo de cadenas, limpieza de datos y normalización.
"""