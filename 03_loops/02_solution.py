number_start, number_end = int(input("Enter range(start, end): ")), int(input("Enter range(start, end): "))

# n = int(input("Enter number for sum of even numnber: "))

sum_of_even_num = 0

for num in range(number_start, number_end + 1):
    if (num % 2 == 0):
        sum_of_even_num += num

print(sum_of_even_num)
