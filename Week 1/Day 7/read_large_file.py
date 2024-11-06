# Reading a large file line-by-line
with open("large_file.txt", "r") as file:
    for line in file:
        print(line.strip())  # Output: Prints each line of large_file.txt
