# Reading a file in 'r' mode
with open("sample.txt", "r") as file:
    print(file.read())

# Writing to a file in 'w' mode
with open("output.txt", "w") as file:
    file.write("This is written in write mode.")

# Appending to a file in 'a' mode
with open("output.txt", "a") as file:
    file.write("\nThis is appended in append mode.")
