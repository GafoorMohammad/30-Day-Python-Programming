# Basic try-except block to handle division by zero
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
