age = int(input("Enter your age: "))

if age<0:
    print("Your age not vaild ")
elif age<18 and age>0:

    print("Your are not eligible for voting")
elif age >= 18 and age <=130:

    print("You are eligible for voting.")
else:
    print("You are age is invaild.")