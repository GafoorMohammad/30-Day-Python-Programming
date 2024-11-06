# Dictionary comprehension to create a dictionary of squares
numbers = [1, 2, 3, 4, 5]
squares_dict = {x: x**2 for x in numbers}
print(squares_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
