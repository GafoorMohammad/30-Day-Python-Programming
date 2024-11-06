# List comprehension with multiple iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [x * y for x in list1 for y in list2]
print(combined)  # Output: [4, 5, 6, 8, 10, 12, 12, 15, 18]
