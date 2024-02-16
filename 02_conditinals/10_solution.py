pet = input("Enter pet (Dog or Cat): ")
age_of_pet = int(input("Enter age of the pet: "))

if (pet == "Dog" and age_of_pet < 2):
    food = "Puppy food"
elif (pet == "Cat" and age_of_pet > 5):
    food = "Senior cat food"

print(f"{food} is recommended for your {pet}.")
