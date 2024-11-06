# Appending to a file
with open("output.txt", "a") as file:
    file.write("This is an appended line.\n")

# Verify the content
with open("output.txt", "r") as file:
    print(file.read())  # Output: Line 1\nLine 2\nLine 3\nThis is an appended line.
