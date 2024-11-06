# Writing multiple lines to a file
with open("output.txt", "w") as file:
    lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
    file.writelines(lines)

# Verify the content
with open("output.txt", "r") as file:
    print(file.read())  # Output: Line 1\nLine 2\nLine 3
