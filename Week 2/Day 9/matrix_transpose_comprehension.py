# Transposing a 2D matrix using list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
