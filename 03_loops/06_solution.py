number = int(input("Enter number for it's factorial: "))
number1 = number

factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print("Factorial of", number1, "is", factorial)
