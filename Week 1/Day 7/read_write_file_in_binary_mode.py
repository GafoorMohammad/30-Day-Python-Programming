# Reading and writing binary files
with open("sample_image.jpg", "rb") as file:
    content = file.read()

with open("output_image.jpg", "wb") as file:
    file.write(content)
