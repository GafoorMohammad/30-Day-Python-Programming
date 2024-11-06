# Nested list comprehension to flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [item for sublist in matrix for item in sublist]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
