def outer_function():
    outer_variable = "Outer"

    def inner_function():
        inner_variable = "Inner"
        print("Inside inner:", outer_variable, inner_variable)

    inner_function()
    # Trying to access inner_variable here will raise an error.
    print("Inside outer:", outer_variable)

outer_function()
