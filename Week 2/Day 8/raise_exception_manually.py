# Raising an exception manually
def check_value(val):
    if val < 0:
        raise ValueError("Value cannot be negative!")
    else:
        print("Valid value.")

try:
    check_value(-1)
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Value cannot be negative!
