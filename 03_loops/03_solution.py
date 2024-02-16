number = int(input("Enter number for it's multipliation table: "))

for i in range(1, 11):
    if i == 5:
        continue
    print(f"{number} x {i} = {number * i}")
