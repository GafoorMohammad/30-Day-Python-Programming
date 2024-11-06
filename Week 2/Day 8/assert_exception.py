# Using assertions to handle error conditions
def positive_number(num):
    assert num > 0, "Number must be positive!"
    print(f"Number is {num}")

try:
    positive_number(-1)
except AssertionError as e:
    print(f"AssertionError: {e}")  # Output: AssertionError: Number must be positive!
