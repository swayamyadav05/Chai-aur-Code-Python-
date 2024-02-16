score = int(input("Enter marks from (0-100): "))

if score >=101:
    print("Please verify your grade again.")
    # quit()
    exit()
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:",grade)

