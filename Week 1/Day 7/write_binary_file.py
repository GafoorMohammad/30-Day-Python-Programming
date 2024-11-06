# Writing to a binary file
data = bytearray([65, 66, 67, 68, 69])  # ASCII values for 'ABCDE'
with open("output_binary.bin", "wb") as file:
    file.write(data)

# Verify the content by reading the binary file
with open("output_binary.bin", "rb") as file:
    print(file.read())  # Output: b'ABCDE'
