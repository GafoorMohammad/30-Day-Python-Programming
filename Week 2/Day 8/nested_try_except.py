# Nested try-except block for handling multiple exceptions
try:
    num1 = 10
    num2 = 0
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Nested Error: Division by zero inside inner try block!")
except Exception as e:
    print(f"Outer Error: {e}")
