# Exception chaining
try:
    x = int(input("Enter a number: "))
    if x < 0:
        raise ValueError("Value cannot be negative")
except ValueError as e:
    raise RuntimeError("An error occurred during input handling") from e
