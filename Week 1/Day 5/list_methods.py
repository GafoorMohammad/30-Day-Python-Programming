numbers = [1, 2, 3, 4]

# Append adds an item at the end
numbers.append(5)
print(numbers)  # Output: [1, 2, 3, 4, 5]

# Remove a specific item
numbers.remove(3)
print(numbers)  # Output: [1, 2, 4, 5]

# Insert an item at a specific index
numbers.insert(2, 10)
print(numbers)  # Output: [1, 2, 10, 4, 5]

# Pop removes the last item by default or item at an index
last_item = numbers.pop()
print(numbers, last_item)  # Output: [1, 2, 10, 4] 5
