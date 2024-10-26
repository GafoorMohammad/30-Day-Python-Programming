# Basic string manipulation
text = "Hello, Python!"
print("Original text:", text)

# String length
print("Length of text:", len(text))

# Uppercase and lowercase
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# Slicing
print("First 5 characters:", text[:5])
print("Last 7 characters:", text[-7:])

# Find and replace
new_text = text.replace("Python", "World")
print("Replaced text:", new_text)

# String formatting with f-strings
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
