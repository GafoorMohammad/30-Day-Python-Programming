# List comprehension to extract vowels from a string
text = "Hello World"
vowels = [char for char in text if char in 'aeiouAEIOU']
print(vowels)  # Output: ['e', 'o', 'o']
