# Using the 'else' block to handle code when no exception occurs
try:
    num1 = 10
    num2 = 5
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    print(f"Result: {result}")  # Output: Result: 2.0
