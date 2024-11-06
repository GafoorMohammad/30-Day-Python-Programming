# Writing and reading from a file using context manager
with open("output.txt", "w") as file:
    file.write("This is a file with context manager.\n")

with open("output.txt", "r") as file:
    content = file.read()
    print(content)  # Output: This is a file with context manager.
