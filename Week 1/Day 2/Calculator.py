# Simple Calculator

def calculator():
    print("Welcome to the Simple Calculator!")
    
    # Prompt user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("\nSelect an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    # Take user input for operation
    operation = input("Enter operation (1/2/3/4): ")

    # Perform calculation based on user choice
    if operation == '1':
        result = num1 + num2
        print(f"\n{num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"\n{num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"\n{num1} * {num2} = {result}")
    elif operation == '4':
        # Check for division by zero
        if num2 != 0:
            result = num1 / num2
            print(f"\n{num1} / {num2} = {result}")
        else:
            print("\nError! Division by zero is not allowed.")
    else:
        print("\nInvalid operation. Please select 1, 2, 3, or 4.")

# Call the calculator function to run the program
calculator()
