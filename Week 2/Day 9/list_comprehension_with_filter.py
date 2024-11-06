# List comprehension with a condition to filter odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers)  # Output: [1, 3, 5, 7, 9]
