import time

# Traditional for loop
start = time.time()
squares = []
for i in range(1000000):
    squares.append(i**2)
end = time.time()
print(f"Traditional loop took: {end - start:.6f} seconds")

# List comprehension
start = time.time()
squares = [i**2 for i in range(1000000)]
end = time.time()
print(f"List comprehension took: {end - start:.6f} seconds")
