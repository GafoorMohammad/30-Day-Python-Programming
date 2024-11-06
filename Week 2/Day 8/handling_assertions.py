# Handle assertions
try:
    x = int(input("Enter a number (greater than 0): "))
    assert x > 0, "Number must be greater than 0"
    print(f"Number is: {x}")
except AssertionError as e:
    print(f"AssertionError: {e}")
