# Set operations with dictionary keys
set_a = {1, 2, 3, 4}
dictionary = {1: "apple", 2: "banana", 3: "cherry"}

# Checking if set elements are in dictionary keys
print(set_a.issubset(dictionary.keys()))  # Output: True

# Getting the intersection of set and dictionary keys
print(set_a & dictionary.keys())  # Output: {1, 2, 3}
