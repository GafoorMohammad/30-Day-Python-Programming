# Counting the number of lines in a file
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(f"The file has {len(lines)} lines.")
