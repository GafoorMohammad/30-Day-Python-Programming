# Handling division by zero gracefully
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed. Returning None.")
        return None

print(divide_numbers(10, 0))  # Output: Error: Division by zero is not allowed. Returning None.
