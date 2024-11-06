# Flattening a 3D list using list comprehension
lists = [[[1], [2]], [[3], [4]], [[5], [6]]]
flat_list = [item for sublist1 in lists for sublist2 in sublist1 for item in sublist2]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]
