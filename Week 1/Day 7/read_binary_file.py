# Reading a binary file (e.g., an image or non-text file)
with open("sample_image.jpg", "rb") as file:
    content = file.read()
    print(content[:20])  # Output: First 20 bytes of the binary file
