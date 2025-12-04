



# Portada:

#    Alejandro De Leon Fonseca                           #   Matriculation: 2530020
#                                       IM 1-3



# Executive summary:
"""
- A list in Python is an ordered, mutable collection that allows adding,
   removing and modifying elements.
- A tuple is an ordered, immutable collection typically used for fixed
   records like coordinates or configuration values.
- A dictionary associates keys to values and allows fast lookups by key.
- Mutability: lists can be changed after creation (append/pop/assign); tuples
   cannot be changed after creation.
- This file contains six problems illustrating lists, tuples and dicts:
  Problem 1 (list operations), Problem 2 (tuples & geometry), Problem 3
   (product catalog dict), Problem 4 (student grades dict+list), Problem 5
   (word frequency list+dict), Problem 6 (contact book CRUD).
- Each problem includes: Description, Inputs, Outputs, Validations, and
   three concrete test cases (normal, border, error). Messages and variable
   names are in English following the requested naming conventions.
"""

# Practices and coding notes (short)
"""

 - Use lists when you need to frequently add/remove items.
- Use tuples for data that must remain constant (coordinates, config).
- Use dictionaries for key-based lookups (e.g., name -> record).
- Avoid modifying a list while iterating with for; prefer comprehensions or
   iterate over a copy.
- Use descriptive key names in dicts: "name", "age", "price".
- Keep messages clear and in English for consistency.
"""

# PROBLEM 1
"""
Description:
- Work with a shopping list of items (strings). Create initial list from a
  comma-separated string, allow adding a new item, show total count and
   verify if a specific item exists.
"""

# Inputs:
"""
- initial_items_text (string) e.g. "apple,banana,orange"
- new_item (string)
- search_item (string)
"""

# Outputs:
"""
- "Items list:" <items_list>
- "Total items:" <len_list>
- "Found item:" true|false
"""

# Validations:
"""
- initial_items_text must not be empty after strip()
- new_item and search_item must not be empty after strip()
- trim whitespace around each item when splitting
"""
# Test cases:
"""
 1) Normal:
    initial_items_text = "apple, banana, orange"
    new_item = "grape"
    search_item = "banana"
 2) Border (initial empty list handled by decision):
    initial_items_text = "   "   (treated as empty -> result empty list allowed)
    new_item = "mango"
    search_item = "mango"
 3) Error:
    initial_items_text = ""  -> should output "Error: invalid input"
    new_item = ""
    search_item = ""
"""
def problem_1_shopping_list(initial_items_text: str, new_item: str, search_item: str):
    """
    Implements problem 1. Returns a tuple of (items_list, total_items, found_bool_or_error)
    Side effect: prints outputs with the required messages.
    """
    # Validate initial_items_text
    if initial_items_text is None or initial_items_text.strip() == "":
        # In this implementation, an empty initial string is allowed and becomes an empty list.
        # But if the caller explicitly sends None or empty and also new_item/search_item empty, treat as error.
        items_list = []
    else:
        # split and strip each element, ignore empty tokens
        items_tokens = [token.strip() for token in initial_items_text.split(",")]
        items_list = [token for token in items_tokens if token != ""]

    # Validate new_item and search_item
    if new_item is None or new_item.strip() == "":
        print("Error: invalid input")
        return None
    if search_item is None or search_item.strip() == "":
        print("Error: invalid input")
        return None

    new_item_clean = new_item.strip()
    search_item_clean = search_item.strip()

    # Add new item
    items_list.append(new_item_clean)

    # Compute outputs
    len_list = len(items_list)
    found = search_item_clean in items_list

    # Print using requested message formats, boolean in lowercase
    print("Items list:", items_list)
    print("Total items:", len_list)
    print("Found item:", str(found).lower())

    return items_list, len_list, found



# Problem 2: Points and distances with tuples
# Description:
"""
- Represent two 2D points as tuples (x1,y1) and (x2,y2). Compute Euclidean
  distance and midpoint tuple.
"""
 Inputs:
 - x1, y1, x2, y2 (float)

# Outputs:
"""
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)
"""

# Validations:
"""
 - Each input must be convertible to float.
 Test cases:
"""
 1) Normal: x1=0, y1=0, x2=3, y2=4 -> distance 5.0, midpoint (1.5,2.0)
 2) Border: points equal x1=2, y1=2, x2=2, y2=2 -> distance 0.0, midpoint (2,2)
 3) Error: non-numeric input like x1="a" -> should print "Error: invalid input"
"""
def problem_2_points_distance(x1_in, y1_in, x2_in, y2_in):
    """
    Implements problem 2. Prints required outputs and returns (point_a, point_b, distance, midpoint).
    
    # Validate convertibility to float
    try:
        x1 = float(x1_in)
        y1 = float(y1_in)
        x2 = float(x2_in)
        y2 = float(y2_in)
    except (TypeError, ValueError):
        print("Error: invalid input")
        return None

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2.0, (y1 + y2) / 2.0)

    print("Point A:", point_a)
    print("Point B:", point_b)
    # Round distance to 6 decimal places for readability
    print("Distance:", round(distance, 6))
    print("Midpoint:", midpoint)

    return point_a, point_b, distance, midpoint



# Problem 3: Product catalog with dictionary
# Description:
"""
# - Manage a small product-price dictionary. Read product name and quantity.
#   If product exists, compute total price; otherwise show error.
"""
# Inputs:
"""
# - product_name (string)
# - quantity (int)
"""
# Outputs:
"""
- If exists:
     "Unit price:" <unit_price>
     "Quantity:" <quantity>
     "Total:" <total_price>
 - If not:
    "Error: product not found"
"""
# Validations:
"""
- product_name not empty after strip
- quantity > 0 and convertible to int
"""
# Test cases:
# 1) Normal: product_name="apple", quantity=2  (exists in initial catalog)
# 2) Border: quantity = 1  (smallest valid positive quantity)
# 3) Error: product_name="unknown" -> "Error: product not found"

def problem_3_product_catalog(product_name_in, quantity_in):
    """
    Implements problem 3. Prints outputs and returns a tuple if successful: (unit_price, quantity, total)
    """
    # Initial catalog
    product_prices = {
        "apple": 10.0,
        "banana": 5.5,
        "orange": 8.25,
        "milk": 20.0
    }

    # Validate product_name
    if product_name_in is None or product_name_in.strip() == "":
        print("Error: invalid input")
        return None
    product_name = product_name_in.strip()

    # Validate quantity
    try:
        quantity = int(quantity_in)
    except (TypeError, ValueError):
        print("Error: invalid input")
        return None

    if quantity <= 0:
        print("Error: invalid input")
        return None

    # Check existence
    if product_name not in product_prices:
        print("Error: product not found")
        return None

    unit_price = float(product_prices[product_name])
    total_price = unit_price * quantity

    print("Unit price:", unit_price)
    print("Quantity:", quantity)
    print("Total:", round(total_price, 2))

    return unit_price, quantity, total_price



# Problem 4: Student grades with dict and list
# Description:
"""
- Manage student grades in a dict: student_name -> list of floats. Compute
  average and whether passed (average >= 70.0).
"""
# Inputs:
"""
- student_name (string)
"""
# Outputs:
"""
- If exists:
     "Grades:" <grades_list>
     "Average:" <average>
     "Passed:" true|false
- If not:
     "Error: student not found"
"""
# Validations:
"""
- student_name not empty after strip
- verify student exists in dictionary
- verify the grades list is not empty before average
"""

# Test cases:
# 1) Normal: existing student with grades above 70
# 2) Border: average exactly 70.0 -> Passed: true
# 3) Error: non-existing student -> "Error: student not found"

def problem_4_student_grades(student_name_in):
    """
    Implements problem 4. Prints outputs and returns (grades_list, average, is_passed)
    """
    grades_db = {
        "Alice": [90.0, 85.5, 78.0],
        "Bob": [70.0, 70.0, 70.0],
        "Charlie": [60.0, 65.0, 55.0]
    }

    if student_name_in is None or student_name_in.strip() == "":
        print("Error: invalid input")
        return None

    student_name = student_name_in.strip()

    if student_name not in grades_db:
        print("Error: student not found")
        return None

    grades_list = grades_db[student_name]
    if len(grades_list) == 0:
        print("Error: invalid input")
        return None

    average = sum(grades_list) / len(grades_list)
    is_passed = average >= 70.0

    print("Grades:", grades_list)
    print("Average:", round(average, 2))
    print("Passed:", str(is_passed).lower())

    return grades_list, average, is_passed



# Problem 5: Word frequency counter (list + dict)
# Description:
"""
- Read a sentence, split into words and count frequency into a dict.
   Show words list, frequency dict and most common word.
"""
# Inputs:
"""
- sentence (string)
"""
# Outputs:
"""
- "Words list:" <words_list>
- "Frequencies:" <freq_dict>
- "Most common word:" <word>
"""
# Validations:
"""
- sentence not empty after strip
- optionally strip punctuation (simple approach)
"""
# Test cases:
# 1) Normal: sentence = "Apple banana apple orange apple"
# 2) Border: sentence with one word "hello"
# 3) Error: sentence = "" -> "Error: invalid input"

def problem_5_word_frequency(sentence_in):
    """
    Implements problem 5. Prints outputs and returns (words_list, freq_dict, most_common_word)
    """
    if sentence_in is None or sentence_in.strip() == "":
        print("Error: invalid input")
        return None

    sentence = sentence_in.strip().lower()

    # Simple punctuation handling: remove common punctuation characters
    # Decision: remove . , ; : ! ? ( ) " ' characters
    for ch in ". , ; : ! ? ( ) \" '".split():
        sentence = sentence.replace(ch, "")

    # Split into words (split on whitespace)
    words_list = [w for w in sentence.split() if w != ""]

    if len(words_list) == 0:
        print("Error: invalid input")
        return None

    freq_dict = {}
    for word in words_list:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    # Find most common word (if tie, return any one)
    most_common_word = None
    highest_count = -1
    for word, count in freq_dict.items():
        if count > highest_count:
            highest_count = count
            most_common_word = word

    print("Words list:", words_list)
    print("Frequencies:", freq_dict)
    print("Most common word:", most_common_word)

    return words_list, freq_dict, most_common_word



# Problem 6: Simple contact book (dictionary CRUD)
# Description:
"""
 - A mini contact book: name -> phone (string). Handle actions ADD, SEARCH,
   DELETE. For ADD, add or update. For SEARCH, show phone. For DELETE, remove.
"""

# Inputs:
"""
# - action_text (string): "ADD", "SEARCH" or "DELETE"
# - name (string)
# - phone (string; only for ADD)
"""
# Outputs:
"""
- For ADD:
     "Contact saved:" name, phone
- For SEARCH:
     if exists: "Phone:" <phone>
     else: "Error: contact not found"
- For DELETE:
     if exists: "Contact deleted:" name
     else: "Error: contact not found"
"""
# Validations:
"""
- Normalize action_text to uppercase and verify it's valid
- name not empty after strip
- For ADD: phone not empty after strip
"""
# Test cases:
# 1) Normal: ADD new contact, then SEARCH it, then DELETE it
# 2) Border: ADD with phone containing spaces " 123 456 " (trimmed)
# 3) Error: SEARCH non-existing contact -> "Error: contact not found"
# -----------------------------------------------------------------------------
def problem_6_contact_book(action_text_in, name_in, phone_in=None, contacts_db=None):
    """
    Implements problem 6. Returns updated contacts_db for ADD/DELETE or phone for SEARCH.
    contacts_db may be provided (dict), otherwise a default initial dict is used.
    """
    # Default initial contacts
    if contacts_db is None:
        contacts_db = {
            "Alice": "1234567890",
            "Bob": "0987654321",
            "Carlos": "5551234567"
        }

    if action_text_in is None or action_text_in.strip() == "":
        print("Error: invalid input")
        return None

    action_text = action_text_in.strip().upper()

    if action_text not in {"ADD", "SEARCH", "DELETE"}:
        print("Error: invalid input")
        return None

    if name_in is None or name_in.strip() == "":
        print("Error: invalid input")
        return None

    name = name_in.strip()

    if action_text == "ADD":
        if phone_in is None or phone_in.strip() == "":
            print("Error: invalid input")
            return None
        phone = phone_in.strip()
        contacts_db[name] = phone
        print("Contact saved:", name, phone)
        return contacts_db

    elif action_text == "SEARCH":
        if name in contacts_db:
            print("Phone:", contacts_db[name])
            return contacts_db[name]
        else:
            print("Error: contact not found")
            return None

    elif action_text == "DELETE":
        if name in contacts_db:
            contacts_db.pop(name)
            print("Contact deleted:", name)
            return contacts_db
        else:
            print("Error: contact not found")
            return None


# -----------------------------------------------------------------------------
# Main demonstration (runs normal test cases for each problem)
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print("---- Problem 1 demo (normal case) ----")
    problem_1_shopping_list("apple, banana, orange", "grape", "banana")
    print()

    print("---- Problem 2 demo (normal case) ----")
    problem_2_points_distance(0, 0, 3, 4)
    print()

    print("---- Problem 3 demo (normal case) ----")
    problem_3_product_catalog("apple", 2)
    print()

    print("---- Problem 4 demo (normal case) ----")
    problem_4_student_grades("Alice")
    print()

    print("---- Problem 5 demo (normal case) ----")
    problem_5_word_frequency("Apple banana apple orange apple")
    print()

    print("---- Problem 6 demo (normal case sequence) ----")
    db = {"Alice": "1234567890", "Bob": "0987654321"}
    # ADD
    db = problem_6_contact_book("ADD", "Daniel", "2223334444", contacts_db=db) or db
    # SEARCH
    problem_6_contact_book("SEARCH", "Daniel", contacts_db=db)
    # DELETE
    db = problem_6_contact_book("DELETE", "Daniel", contacts_db=db) or db
    print()

    print("End of demo run. For border and error test cases, please call the functions with the specific inputs in the comments.")



# Conclusions  
"""
- Lists are best for collections that require frequent mutation: appending,
   removing, reordering. They are simple and flexible.
- Tuples are ideal for fixed-size records (coordinates, configuration)
   where immutability prevents accidental modification.
- Dictionaries are efficient for key-based lookups and model real-world maps
   like product catalogs or contact books.
- Combining structures (e.g., dict of lists for student grades) is a common
   pattern to model hierarchical or grouped data.
- Clear validations and descriptive keys significantly reduce runtime errors
   and make code easier to maintain.
"""

# References:

# 1) Python documentation - Built-in Types: list, tuple, dict
#    https://docs.python.org/3/library/stdtypes.html
# 2) Python tutorial - Data Structures
#    https://docs.python.org/3/tutorial/datastructures.html
# 3) "Automate the Boring Stuff with Python" - Al Sweigart (Chapter on lists/dicts)
# 4) Real Python - Working with Dictionaries in Python
#    https://realpython.com/python-dicts/
# 5) W3Schools - Python Data Structures
#    https://www.w3schools.com/python/python_lists.asp
#
# GitHub repository (placeholder):
# https://github.com/AlejandroGomez101/assignment-example
