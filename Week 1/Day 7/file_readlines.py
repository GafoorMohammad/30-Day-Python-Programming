# Reading all lines into a list
with open("sample.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # Output: Prints each line of sample.txt
