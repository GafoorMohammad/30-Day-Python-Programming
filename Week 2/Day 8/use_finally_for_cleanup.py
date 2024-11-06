# Using finally for cleanup actions (e.g., closing a file)
try:
    file = open("sample.txt", "r")
    # Perform file operations here
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()  # Ensures file is closed even if an error occurs
    print("File closed.")
