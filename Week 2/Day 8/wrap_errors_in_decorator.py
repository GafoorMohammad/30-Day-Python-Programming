# Wrapping errors in a decorator
def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print("Error: Division by zero!")
        except Exception as e:
            print(f"Error: {e}")
    return wrapper

@error_handler
def divide(num1, num2):
    return num1 / num2

print(divide(10, 0))  # Output: Error: Division by zero!
