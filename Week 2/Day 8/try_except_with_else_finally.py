# Full example with try, except, else, and finally
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ZeroDivisionError as e:
    print(f"Error: {e}")
except ValueError as e:
    print("Invalid input. Please enter a valid number.")
else:
    print(f"Division result: {y}")
finally:
    print("Execution completed.")
