# Reading a file line by line
with open("sample.txt", "r") as file:
    line = file.readline()
    while line:
        print(line.strip())  # Output: Prints each line of sample.txt
        line = file.readline()
