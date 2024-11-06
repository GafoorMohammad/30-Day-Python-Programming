import csv

# Writing CSV data to a file
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])
    writer.writerow(["Bob", 30, "Los Angeles"])

# Reading the CSV file
with open("data.csv", "r") as file:
    content = file.read()
    print(content)
