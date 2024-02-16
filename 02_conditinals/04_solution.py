fruit = input("Enter a fruit: ")
colour = input("Which colour is it right now: ")

if colour == "Green":
    level = "Unripe"
elif colour == "Yellow":
    level = "Ripe"
elif colour == "Brown":
    level = "Overripe"

print(f"The {fruit} is {level}")
