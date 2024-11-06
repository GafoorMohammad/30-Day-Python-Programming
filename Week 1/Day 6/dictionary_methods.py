# Creating a dictionary
fruits = {"apple": 3, "banana": 2, "cherry": 5}

# Using get() to access values safely
print(fruits.get("apple"))  # Output: 3
print(fruits.get("orange", "Not Found"))  # Output: Not Found

# Getting all keys, values, and items
print(fruits.keys())  # Output: dict_keys(['apple', 'banana', 'cherry'])
print(fruits.values())  # Output: dict_values([3, 2, 5])
print(fruits.items())  # Output: dict_items([('apple', 3), ('banana', 2), ('cherry', 5)])
