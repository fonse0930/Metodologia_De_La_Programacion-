# Portada:
#   Name: Alejandro De Leon Fonseca                         Matriculation: 2530020
#                                       Group: IM 1-3

# Executive summary:
"""
- A for loop iterates a known number of times, typically used to traverse ranges
  or sequences (for i in range(1, n+1) or for item in my_list).
- A while loop repeats while a condition holds; it is natural when the number
   of iterations depends on runtime conditions (sentinels, user input).
- A counter tracks occurrences (count = count + 1) and an accumulator sums
   values (total = total + value) inside loops.
- Defining a clear exit condition avoids infinite loops; update control
   variables inside while loops and consider safety limits.
- This file contains six problems showcasing for and while usage:
   Problem 1 (sum with for+range), Problem 2 (multiplication table with for),
   Problem 3 (average with while sentinel), Problem 4 (password attempts with while),
   Problem 5 (simple menu with while), Problem 6 (pattern printing with nested loops).
"""

# Principles and good practices (short)

"""
 Use for when the number of iterations is known (e.g., range).
 Use while when iterations depend on conditions or user input (sentinel).
 Initialize counters and accumulators before loops.
 Update control variables inside while loops to avoid infinite loops.
 Keep loop bodies small; extract logic to functions when complex.
"""
#
# Problem 1: Sum of range with for
# Description:
# - Sum all integers from 1 to n inclusive and sum only even numbers in that range.
#
# Inputs:
# - n (int)
#
# Outputs:
# - "Sum 1..n:" <total_sum>
# - "Even sum 1..n:" <even_sum>
#
# Validations:
# - n must be convertible to int and n >= 1
#
# Test cases:
# 1) Normal: n = 10 -> Sum 55, Even sum 30
# 2) Border: n = 1 -> Sum 1, Even sum 0
# 3) Error: n = 0 or n = "a" -> "Error: invalid input"

def problem_1_sum_range(n_in):
    try:
        n = int(n_in)
    except (TypeError, ValueError):
        print("Error: invalid input")
        return None
    if n < 1:
        print("Error: invalid input")
        return None

    total_sum = 0
    even_sum = 0
    # for with range
    for i in range(1, n + 1):
        total_sum += i
        if i % 2 == 0:
            even_sum += i

    print("Sum 1..n:", total_sum)
    print("Even sum 1..n:", even_sum)
    return total_sum, even_sum



# Problem 2: Multiplication table with for
# Description:
# - Print multiplication table for base from 1 to m.
#
# Inputs:
# - base (int)
# - m (int)
#
# Outputs:
# - Lines like "5 x 1 = 5"
#
# Validations:
# - base and m convertible to int, m >= 1
#
# Test cases:
# 1) Normal: base=5, m=4 (prints 5x1..5x4)
# 2) Border: base=2, m=1 (prints single line)
# 3) Error: m=0 or base="a" -> "Error: invalid input"

def problem_2_multiplication_table(base_in, m_in):
    try:
        base = int(base_in)
        m = int(m_in)
    except (TypeError, ValueError):
        print("Error: invalid input")
        return None
    if m < 1:
        print("Error: invalid input")
        return None

    for i in range(1, m + 1):
        product = base * i
        print(f"{base} x {i} = {product}")
    return True



# Problem 3: Average of numbers with while and sentinel
# Description:
# - Read numbers until sentinel_value is entered (-1). Compute count and average.
#
# Inputs:
# - Repeated number inputs (float). sentinel_value is -1 (excluded).
#
# Outputs:
# - "Count:" <count>
# - "Average:" <average_value>
# - If no valid data: "Error: no data"
#
# Validations:
# - Each entry convertible to float. Ignore sentinel in calculations.
#
# Test cases (simulate input via list):
# 1) Normal: [2, 4, 6, -1] -> Count 3, Average 4.0
# 2) Border: [-1] -> Error: no data
# 3) Error: ["a", -1] -> conversion error handled per item -> ignored or error policy

def problem_3_average_sentinel(inputs_list):
    """
    inputs_list: a list of values to simulate repeated user input.
    Returns (count, average) or None if no data.
    """
    sentinel_value = -1
    total = 0.0
    count = 0
    # We'll iterate over provided inputs_list to simulate user entries.
    for entry in inputs_list:
        try:
            number = float(entry)
        except (TypeError, ValueError):
            # Skip invalid entries but report error message
            print("Error: invalid input")
            return None
        if number == sentinel_value:
            break
        total += number
        count += 1

    if count == 0:
        print("Error: no data")
        return None

    average = total / count
    print("Count:", count)
    print("Average:", round(average, 6))
    return count, average



# Problem 4: Password attempts with while
# Description:
# - Allow up to MAX_ATTEMPTS to enter correct password defined in the code.
#
# Inputs:
# - Repeated user_password attempts (strings)
#
# Outputs:
# - "Login success" on correct password
# - "Account locked" if attempts exhausted
#
# Validations:
# - MAX_ATTEMPTS > 0
#
# Test cases (simulate attempts via list):
# 1) Normal: attempts = ["wrong","admin123"] -> Login success
# 2) Border: attempts = ["admin123"] -> Login success at first try
# 3) Error: attempts = ["x","y","z"] with MAX_ATTEMPTS=3 -> Account locked

def problem_4_password_attempts(attempts_list, correct_password="admin123"):
    MAX_ATTEMPTS = 3
    if MAX_ATTEMPTS <= 0:
        print("Error: invalid configuration")
        return None

    attempts = 0
    for attempt in attempts_list:
        attempts += 1
        if attempt == correct_password:
            print("Login success")
            return True
        if attempts >= MAX_ATTEMPTS:
            break

    print("Account locked")
    return False


# Problem 5: Simple menu with while
# Description:
# - Text menu repeating until user chooses 0 (Exit). Options:
#   1) Show greeting
#   2) Show current counter value
#   3) Increment counter
#   0) Exit
#
# Inputs:
# - sequence of option entries (simulate via list)
#
# Outputs:
# - "Hello!" / "Counter:" <counter_value> / "Counter incremented" / "Bye!" / "Error: invalid option"
#
# Validations:
# - Accept only 0,1,2,3. Convert option to int safely.
#
# Test cases:
# 1) Normal: options = [1,2,3,2,0]
# 2) Border: options = [0] -> immediate exit with "Bye!"
# 3) Error: options = [9,0] -> "Error: invalid option" then "Bye!"

def problem_5_simple_menu(options_list):
    counter = 0
    # options_list simulates user inputs
    for opt in options_list:
        try:
            option = int(opt)
        except (TypeError, ValueError):
            print("Error: invalid option")
            continue

        if option == 1:
            print("Hello!")
        elif option == 2:
            print("Counter:", counter)
        elif option == 3:
            counter += 1
            print("Counter incremented")
        elif option == 0:
            print("Bye!")
            break
        else:
            print("Error: invalid option")
    return counter



# Problem 6: Pattern printing with nested loops
# Description:
# - Print right triangle of '*' for n rows. Optionally print inverted pattern.
#
# Inputs:
# - n (int)
#
# Outputs:
# - Lines with increasing stars: "*", "**", ..., "*" * n
# - (Optional) inverted pattern printed after
#
# Validations:
# - n convertible to int and n >= 1
#
# Test cases:
# 1) Normal: n=4 -> prints 1..4 stars
# 2) Border: n=1 -> prints single "*"
# 3) Error: n=0 or n="a" -> "Error: invalid input"

def problem_6_pattern_printing(n_in, print_inverted=False):
    try:
        n = int(n_in)
    except (TypeError, ValueError):
        print("Error: invalid input")
        return None
    if n < 1:
        print("Error: invalid input")
        return None

    # Increasing triangle
    for i in range(1, n + 1):
        print("*" * i)

    if print_inverted:
        # Optional: inverted triangle
        for i in range(n, 0, -1):
            print("*" * i)
    return True



# Main demonstration - runs normal test cases for each problem

if __name__ == "__main__":
    print("---- Problem 1 demo (normal) ----")
    problem_1_sum_range(10)
    print()

    print("---- Problem 2 demo (normal) ----")
    problem_2_multiplication_table(5, 4)
    print()

    print("---- Problem 3 demo (normal) ----")
    # simulate inputs: 2,4,6,-1
    problem_3_average_sentinel([2, 4, 6, -1])
    print()

    print("---- Problem 4 demo (normal) ----")
    # simulate attempts: wrong, admin123
    problem_4_password_attempts(["wrong", "admin123"])
    print()

    print("---- Problem 5 demo (normal) ----")
    # simulate menu options: 1,2,3,2,0
    problem_5_simple_menu([1, 2, 3, 2, 0])
    print()

    print("---- Problem 6 demo (normal) ----")
    problem_6_pattern_printing(4, print_inverted=False)
    print()

    print("End of demo run. Call functions with the commented test cases to run border and error scenarios.")



# Conclusions (5-8 lines)
"""
 - For loops are ideal when the number of iterations is known; while loops
   are better when the termination depends on runtime conditions or user input.
- Counters and accumulators simplify counting and summing inside loops and
   make algorithm complexity explicit.
- The main risk with while loops is creating infinite loops; always update
   control variables and consider sentinel values or safety limits.
- Menus and password attempts are common examples where while loops model
   repeated user interaction naturally.
- Nested loops enable generation of patterns and matrix-like traversals but
   may increase complexity (O(n^2)) and should be used judiciously.
"""

# References:
# 1) Python documentation - for and while statements
#    https://docs.python.org/3/reference/compound_stmts.html#the-for-statement
# 2) Python tutorial - Control Flow Tools
#    https://docs.python.org/3/tutorial/controlflow.html
# 3) Real Python - Python For Loops Explained
#    https://realpython.com/python-for-loop/
# 4) GeeksforGeeks - While Loop in Python
#    https://www.geeksforgeeks.org/while-loops-in-python/
# 5) "Automate the Boring Stuff with Python" - Al Sweigart (loops and programs)
#
# GitHub repository (placeholder):
# https://github.com/AlejandroGomez101/loops-assignment


