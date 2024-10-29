def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(pet_name="Rover")               
# Output: I have a dog named Rover.
describe_pet(animal_type="cat", pet_name="Milo")  
# Output: I have a cat named Milo.
