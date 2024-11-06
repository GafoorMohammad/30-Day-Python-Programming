# Using a function inside a list comprehension
def square(x):
    return x**2

numbers = [1, 2, 3, 4, 5]
squares = [square(x) for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]
