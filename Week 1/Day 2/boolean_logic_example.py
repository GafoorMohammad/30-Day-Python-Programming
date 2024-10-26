age = 25
has_permission = True

# Using `and`, `or`, and `not` operators
if age >= 18 and has_permission:
    print("Access granted")
else:
    print("Access denied")

# Example of `not` operator
is_minor = not (age >= 18)
print("Is minor:", is_minor)

# Combining `and` and `or`
user_role = "admin"
if user_role == "admin" or (age >= 18 and has_permission):
    print("Special access granted")
else:
    print("Regular access")
