
# Portada:
#   Name: Alejandro De Leon Fonseca                         Matriculation: 2530020
#                                       Group: IM 1-3

# Executive summary:
"""
- A function in Python is a reusable block of code defined with def that can
   receive parameters and return values.
- Parameters are the names used in the function definition; arguments are the
  actual values passed when calling the function.
- Separating logic into functions improves reuse, readability and testability.
- A return value lets the caller use the result programmatically instead of
   only printing; pure functions (no side effects) are easier to test. 
- This document implements six problems: rectangle geometry, grade
   classification, list statistics, discount application, greeting, and factorial.
"""

# Principles and good practices:
"""
- Prefer small functions that do a single job (single responsibility).
- Avoid repeating code: extract repeated logic into helper functions.
- Aim for pure functions when possible (same input -> same output).
- Document each function with comments describing parameters and return values.
- Use descriptive function names (calculate_area, summarize_numbers).
"""

# Problem 1: Rectangle area and perimeter (basic functions)
# Description:
# - Define calculate_area(width, height) and calculate_perimeter(width, height).
# - The main code will validate inputs, call the functions and print results.
#
# Inputs:
# - width (float)
# - height (float)
#
# Outputs:
# - "Area:" <area_value>
# - "Perimeter:" <perimeter_value>
#
# Validations:
# - width > 0, height > 0
# - If invalid: print "Error: invalid input"
#
# Test cases:
# 1) Normal: width=5, height=3 -> Area:15, Perimeter:16
# 2) Border: width=0.1, height=0.1 -> Area:0.01, Perimeter:0.4
# 3) Error: width=-1 or "a" -> "Error: invalid input"

def calculate_area(width, height):
    """
    Returns area = width * height
    Assumes width and height are floats > 0 (validation performed by caller).
    """
    return width * height

def calculate_perimeter(width, height):
    """
    Returns perimeter = 2 * (width + height)
    """
    return 2 * (width + height)



# Problem 2: Grade classifier (function with return string)
# Description:
# - classify_grade(score) returns "A","B","C","D" or "F" according to ranges.
#
# Inputs:
# - score (float or int)
#
# Outputs:
# - "Score:" <score>
# - "Category:" <grade_letter>
#
# Validations:
# - 0 <= score <= 100
# - If invalid: print "Error: invalid input"
#
# Test cases:
# 1) Normal: score=92 -> Category: A
# 2) Border: score=80 -> Category: B
# 3) Error: score=120 or "x" -> "Error: invalid input"

def classify_grade(score):
    """
    Returns grade letter for numeric score in 0..100.
    """
    # Caller must validate numeric range; function assumes numeric input
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"



# Problem 3: List statistics function (min, max, average)
# Description:
# - summarize_numbers(numbers_list) returns a dict with keys "min","max","average"
#
# Inputs:
# - numbers_text (string, comma-separated) -> converted to list of floats
#
# Outputs:
# - "Min:" <min_value>
# - "Max:" <max_value>
# - "Average:" <average_value>
#
# Validations:
# - numbers_text not empty after strip
# - all elements convertible to float
# - list non-empty after conversion
#
# Test cases:
# 1) Normal: "10,20,30" -> Min:10, Max:30, Average:20
# 2) Border: "5" -> Min:5, Max:5, Average:5
# 3) Error: "" or "10,a,20" -> "Error: invalid input"

def summarize_numbers(numbers_list):
    """
    numbers_list: list of numbers (int/float)
    returns: dict {"min":..., "max":..., "average":...}
    """
    if numbers_list is None or len(numbers_list) == 0:
        raise ValueError("invalid input")
    # compute values
    min_value = min(numbers_list)
    max_value = max(numbers_list)
    average_value = sum(numbers_list) / len(numbers_list)
    return {"min": min_value, "max": max_value, "average": average_value}


def parse_numbers_text(numbers_text):
    """
    Helper: parse comma-separated string into list of floats.
    Raises ValueError on invalid input.
    """
    if numbers_text is None or numbers_text.strip() == "":
        raise ValueError("invalid input")
    tokens = [t.strip() for t in numbers_text.split(",")]
    nums = []
    for tok in tokens:
        if tok == "":
            raise ValueError("invalid input")
        try:
            num = float(tok)
        except (TypeError, ValueError):
            raise ValueError("invalid input")
        nums.append(num)
    if len(nums) == 0:
        raise ValueError("invalid input")
    return nums



# Problem 4: Apply discount list (pure function)
# Description:
# - apply_discount(prices_list, discount_rate) returns a new list with discounted prices.
#
# Inputs:
# - prices_text (string e.g. "100,200")
# - discount_rate (float in [0,1])
#
# Outputs:
# - "Original prices:" <original_list>
# - "Discounted prices:" <discounted_list>
#
# Validations:
# - prices_text not empty and prices > 0
# - 0 <= discount_rate <= 1
#
# Test cases:
# 1) Normal: "100,200", 0.1 -> [100,200], [90,180]
# 2) Border: "0.01", 0 -> original [0.01], discounted [0.01]
# 3) Error: discount_rate = -0.1 or prices_text contain -10 -> "Error: invalid input"

def apply_discount(prices_list, discount_rate):
    """
    prices_list: list of floats (prices > 0)
    discount_rate: float in [0,1]
    Returns a new list with discounted prices (does not modify input).
    """
    if prices_list is None or len(prices_list) == 0:
        raise ValueError("invalid input")
    if not (0 <= discount_rate <= 1):
        raise ValueError("invalid input")
    discounted = []
    for price in prices_list:
        if price < 0:
            raise ValueError("invalid input")
        discounted_price = price * (1 - discount_rate)
        discounted.append(round(discounted_price, 6))
    return discounted


def parse_prices_text(prices_text):
    """
    Helper: parse comma-separated prices string into list of floats.
    Raises ValueError on invalid input.
    """
    if prices_text is None or prices_text.strip() == "":
        raise ValueError("invalid input")
    toks = [t.strip() for t in prices_text.split(",")]
    prices = []
    for t in toks:
        if t == "":
            raise ValueError("invalid input")
        try:
            p = float(t)
        except (TypeError, ValueError):
            raise ValueError("invalid input")
        prices.append(p)
    if len(prices) == 0:
        raise ValueError("invalid input")
    return prices



# Problem 5: Greeting function with default parameters
# Description:
# - greet(name, title="") returns "Hello, <full_name>!"
#
# Inputs:
# - name (string)
# - title (string, optional)
#
# Outputs:
# - "Greeting:" <greeting_message>
#
# Validations:
# - name not empty after strip
#
# Test cases:
# 1) Normal: name="Alice", title="Dr." -> "Hello, Dr. Alice!"
# 2) Border: title="" -> "Hello, Alice!"
# 3) Error: name="" -> "Error: invalid input"

def greet(name, title=""):
    """
    Returns greeting string. title is optional.
    """
    if name is None or name.strip() == "":
        raise ValueError("invalid input")
    name_clean = name.strip()
    title_clean = title.strip() if title is not None else ""
    if title_clean != "":
        full_name = f"{title_clean} {name_clean}"
    else:
        full_name = name_clean
    return f"Hello, {full_name}!"



# Problem 6: Factorial function (iterative)
# Description:
# - factorial(n) returns n! implemented iteratively to avoid recursion depth issues.
#
# Inputs:
# - n (int)
#
# Outputs:
# - "n:" <n>
# - "Factorial:" <factorial_value>
#
# Validations:
# - n integer, n >= 0, n <= 20 (to avoid very large results)
#
# Test cases:
# 1) Normal: n=5 -> 120
# 2) Border: n=0 -> 1
# 3) Error: n=-1 or n=21 -> "Error: invalid input"

def factorial(n):
    """
    Iterative factorial to compute n! for n >= 0
    Limits n <= 20 for safety (fits in 64-bit range comfortably).
    """
    if not isinstance(n, int):
        raise ValueError("invalid input")
    if n < 0 or n > 20:
        raise ValueError("invalid input")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result



# Main code: calls to functions with test values (demonstration)

if __name__ == "__main__":
    # Problem 1 demo
    print("---- Problem 1 demo ----")
    try:
        width_val = 5.0
        height_val = 3.0
        if width_val <= 0 or height_val <= 0:
            print("Error: invalid input")
        else:
            area_val = calculate_area(width_val, height_val)
            perimeter_val = calculate_perimeter(width_val, height_val)
            print("Area:", area_val)
            print("Perimeter:", perimeter_val)
    except Exception:
        print("Error: invalid input")
    print()

    # Problem 2 demo
    print("---- Problem 2 demo ----")
    try:
        score_val = 92
        if not (0 <= score_val <= 100):
            print("Error: invalid input")
        else:
            category = classify_grade(score_val)
            print("Score:", score_val)
            print("Category:", category)
    except Exception:
        print("Error: invalid input")
    print()

    # Problem 3 demo
    print("---- Problem 3 demo ----")
    try:
        numbers_text = "10,20,30"
        nums = parse_numbers_text(numbers_text)
        summary = summarize_numbers(nums)
        print("Min:", summary["min"])
        print("Max:", summary["max"])
        print("Average:", round(summary["average"], 6))
    except ValueError:
        print("Error: invalid input")
    print()

    # Problem 4 demo
    print("---- Problem 4 demo ----")
    try:
        prices_text = "100,200,300"
        discount_rate = 0.10
        prices = parse_prices_text(prices_text)
        discounted = apply_discount(prices, discount_rate)
        print("Original prices:", prices)
        print("Discounted prices:", discounted)
    except ValueError:
        print("Error: invalid input")
    print()

    # Problem 5 demo
    print("---- Problem 5 demo ----")
    try:
        greeting = greet("Alice", title="Dr.")
        print("Greeting:", greeting)
    except ValueError:
        print("Error: invalid input")
    print()

    # Problem 6 demo
    print("---- Problem 6 demo ----")
    try:
        n_val = 5
        fact_val = factorial(n_val)
        print("n:", n_val)
        print("Factorial:", fact_val)
    except ValueError:
        print("Error: invalid input")
    print()

    print("End of demo run. Use the functions with the commented test cases for border and error scenarios.")


# Conclusions
"""
- Functions help organize code into reusable, focused units and make testing simpler.
- Returning values (instead of only printing) enables further programmatic use
   of results and improves testability.
- Default parameters and named arguments increase flexibility and readability.
- Encapsulating repeated logic in helpers (parse_*, summarize_*) reduces bugs.
- Separating main program flow from function definitions clarifies responsibilities.
"""
#
# References:
# 1) Python documentation - Defining functions
#    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# 2) Python docs - Function definitions
#    https://docs.python.org/3/reference/compound_stmts.html#function-definitions
# 3) Real Python - Defining Your Own Python Function
#    https://realpython.com/defining-your-own-python-function/
# 4) Automate the Boring Stuff with Python - Functions chapter
#    https://automatetheboringstuff.com/
# 5) GeeksforGeeks - Python Functions
#    https://www.geeksforgeeks.org/python-functions/
#
# GitHub repository (placeholder):
# https://github.com/AlejandroGomez101/functions-assignment

