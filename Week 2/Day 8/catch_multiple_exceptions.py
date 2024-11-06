# Handling multiple exceptions
try:
    num1 = 10
    num2 = "a"  # This will cause a TypeError
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except TypeError:
    print("Error: Invalid operation between different types!")
