# Custom exception class
class InvalidNumberError(Exception):
    pass

try:
    num = -1
    if num < 0:
        raise InvalidNumberError("Negative numbers are not allowed!")
except InvalidNumberError as e:
    print(f"Custom Exception: {e}")
