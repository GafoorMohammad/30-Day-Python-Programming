# Handling invalid user input using try-except
try:
    user_input = int(input("Enter a number: "))
    result = 10 / user_input
    print(f"Result: {result}")
except ValueError:
    print("Error: Please enter a valid integer!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
