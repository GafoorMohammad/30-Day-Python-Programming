# Reverse a list using list comprehension
numbers = [1, 2, 3, 4, 5]
reversed_numbers = [numbers[i] for i in range(len(numbers)-1, -1, -1)]
print(reversed_numbers)  # Output: [5, 4, 3, 2, 1]
