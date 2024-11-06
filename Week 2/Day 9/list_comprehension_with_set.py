# List comprehension to create a set from a list
numbers = [1, 2, 2, 3, 4, 5, 5]
unique_squares = {x**2 for x in numbers}  # Using set comprehension
print(unique_squares)  # Output: {1, 4, 9, 16, 25}
