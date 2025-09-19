# demo_app.py
# Simple Python app for SonarQube POC

import sys


def add_numbers(a, b):
    # Bad practice: using print inside function instead of return
    print("Adding numbers:", a, b)
    return a + b


def divide_numbers(a, b):
    # Bug risk: no zero-division handling
    return a / b


def unused_function():
    # This function is never used (SonarQube will flag it)
    data = "I am unused"
    print(data)


if __name__ == "__main__":
    # Example usage
    x = 10
    y = 0  # Division by zero case (SonarQube can detect bug-prone code)

    result = add_numbers(x, 5)
    print("Result:", result)

    try:
        div_result = divide_numbers(x, y)
        print("Division Result:", div_result)
    except Exception as e:
        print("Error occurred:", e)

    # Hardcoded credentials (Sonar will warn about this)
    password = "admin1277777777777777773"
    print("Password is:", password)
