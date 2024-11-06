# Handle key not found error
my_dict = {'name': 'Alice'}
try:
    print(my_dict['age'])
except KeyError as e:
    print(f"Error: Key not found: {e}")
