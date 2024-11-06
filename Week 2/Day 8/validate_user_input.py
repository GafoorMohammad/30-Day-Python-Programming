# Validating user input with custom exceptions
class InvalidAgeError(Exception):
    pass

def validate_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError("Invalid age provided!")
    else:
        print(f"Age is {age}")

try:
    validate_age(150)
except InvalidAgeError as e:
    print(f"Error: {e}")  # Output: Error: Invalid age provided!
