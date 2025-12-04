
# Portada:
#   Name: Alejandro De Leon Fonseca                         Matriculation: 2530020
#                                        Group: IM 1-3

# Executive summary:
"""
- The Fibonacci series is a sequence where each term after the first two is
   the sum of the two preceding terms: 0, 1, 1, 2, 3, 5, ...
- Calculating the series up to n terms means generating the first n numbers
    starting at 0 (term 1 = 0, term 2 = 1).
- This program reads an integer n, validates it, and generates the first n
   Fibonacci terms using an iterative loop, returning them as a list.
"""

# Problem: Fibonacci series generator
# Description:
#   Program that reads an integer n and prints the first n terms of the
#   Fibonacci series starting at 0 and 1.

# Inputs:
#   - n (int; number of terms to generate)

# Outputs:
#   - "Number of terms:" <n>
#   - "Fibonacci series:" <term_1> <term_2> ... <term_n>

# Validations:
#   - n must be an integer
#   - n must be >= 1
#   - n must be <= 50 (to avoid extremely long outputs); adjust limit if desired
#   - On validation failure print: "Error: invalid input" and do not compute series

# Test cases:
# 1) Normal: n = 5  -> Fibonacci series: 0 1 1 2 3
# 2) Border: n = 1  -> Fibonacci series: 0
# 3) Error:  n = 0  -> Error: invalid input
# 4) Error:  n = -3 -> Error: invalid input
# 5) Error:  n = 51 -> Error: invalid input

# Optional diagram/table (described):
# "Flowchart (text): Read n -> Validate n is integer and 1<=n<=50 -> Call
#  generate_fibonacci(n) -> Print results -> End"

def generate_fibonacci(n):
    """
    Generate the first n Fibonacci numbers (starting with 0, 1).
    Parameters:
        n (int): number of terms to generate (assumed validated: 1 <= n <= 50)
    Returns:
        list of int: Fibonacci series of length n
    """
    # handle n == 1 and n == 2 explicitly for clarity
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    fib_list = [0, 1]
    # iterative loop to generate remaining terms
    for _ in range(2, n):
        next_term = fib_list[-1] + fib_list[-2]
        fib_list.append(next_term)
    return fib_list


def parse_and_validate_input(input_str, max_limit=50):
    """
    Parse input string to integer and validate range.
    Returns integer n if valid, otherwise raises ValueError.
    """
    if input_str is None:
        raise ValueError("invalid input")
    try:
        n = int(input_str)
    except (TypeError, ValueError):
        raise ValueError("invalid input")

    if n < 1 or n > max_limit:
        raise ValueError("invalid input")
    return n


if __name__ == "__main__":
    # Read n from standard input
    # (User may provide input when running the script, e.g., via terminal)
    try:
        raw_input_value = input().strip()
    except Exception:
        print("Error: invalid input")
        raise SystemExit(1)

    # Validate and parse
    try:
        n_terms = parse_and_validate_input(raw_input_value, max_limit=50)
    except ValueError:
        print("Error: invalid input")
        raise SystemExit(1)

    # Generate Fibonacci series
    fibonacci_series = generate_fibonacci(n_terms)

    # Output results in the requested format
    print("Number of terms:", n_terms)
    # Join terms with space
    print("Fibonacci series:", " ".join(str(x) for x in fibonacci_series))


# Conclusions:
# - Using an iterative loop (for) made generation simple and efficient (O(n)).
# - Handling n = 1 and n = 2 explicitly avoids index errors and clarifies edge cases.
# - The generate_fibonacci function can be reused in other programs (e.g., for
#   analyzing growth, computing ratios, or feeding into visualizations).


# References:
# 1) Python documentation - for and while loops: https://docs.python.org/3/tutorial/controlflow.html
# 2) Weisstein, Eric W. "Fibonacci Number." From MathWorld--A Wolfram Web Resource.
# 3) Knuth, D. E. "The Art of Computer Programming" (sections on recurrence relations and sequences).
 
