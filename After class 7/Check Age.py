# Get age input from the user
age = int(input("Enter your age: "))

# Check if the age is greater than or equal to 10
if age >= 10:
    # Nested check: is also less than or equal to 19?
    if age <= 19:
        print("The age you entered is between 10 and 19.")
        print("so you are a teenager.")
    else:
        print("The age you entered is greater than 19.")
        print("You are an adult.")
else:
    print("The age you entered is less than 10.")
    print("You are a child.")        