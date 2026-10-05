age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")

elif age >= 18 and age<=120:
    print("You are eligible for voting")

else:
    print("You are not eligible for voting")