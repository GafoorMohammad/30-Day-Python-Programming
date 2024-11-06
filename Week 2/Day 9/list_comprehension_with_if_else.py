# List comprehension with if-else to label numbers as even or odd
numbers = [1, 2, 3, 4, 5]
labels = ['even' if x % 2 == 0 else 'odd' for x in numbers]
print(labels)  # Output: ['odd', 'even', 'odd', 'even', 'odd']
