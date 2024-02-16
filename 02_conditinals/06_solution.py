distance = int(input("Enter distance in km: "))

if distance < 3:
    mode = "Walk"
elif distance <= 15:
    mode = "Bike"
elif distance > 15:
    mode = "Car"
    
print("AI recommends you the transport of:", mode)
