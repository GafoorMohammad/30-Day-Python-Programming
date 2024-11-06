# Writing to a file
with open("output.txt", "w") as file:
    file.write("Hello, this is a test.\nWelcome to File I/O!")

# Verify the content
with open("output.txt", "r") as file:
    print(file.read())  # Output: Hello, this is a test.\nWelcome to File I/O!
