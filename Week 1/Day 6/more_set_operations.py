# Creating sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Symmetric Difference (elements in either set, but not both)
print(set_a ^ set_b)  # Output: {1, 2, 5, 6}

# Checking if a set is a superset of another
print(set_a.issuperset({1, 2}))  # Output: True
