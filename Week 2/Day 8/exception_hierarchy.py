# Handle exception hierarchy
try:
    x = int(input("Enter a number: "))
    if x < 0:
        raise ValueError("Negative value!")
    elif x == 0:
        raise ArithmeticError("Zero value!")
except ArithmeticError as e:
    print(f"Arithmetic error: {e}")
except ValueError as e:
    print(f"Value error: {e}")
except Exception as e:
    print(f"General error: {e}")
