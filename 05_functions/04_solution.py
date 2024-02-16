# Function Returning Multiples Values
import math

def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

radius = int(input("Enter the radius: "))
a, c = circle(radius)

#Using '%' operator
print("Area: %.2f" %a, "Circumference: %.2f" %c)

# Using format() function
print("Area: {0:.3f}".format(a), "Circumference: {0:.3f}".format(c))

# Using round() function
print("Area:", round(a, 5), "Circumference:", round(c, 5))

