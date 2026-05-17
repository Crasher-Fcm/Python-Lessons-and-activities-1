print("Select your ride")
print("1. Bike")
print("2. Car")
print("3. Bus")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("What type of bike?")
    print("1. Scooty\n")
    print("2. Scooter\n")   

    choice_2 = int(input("Enter your choice: "))
    if choice_2 == 1:
        print("You have selected Scooty")
    else:
        print("You have selected Scooter")

elif (choice ==2):

    print("What type of car?")
    print("1. Sedan\n")
    print("2. Hatchback\n")

    choice_3 = int(input("Enter your choice: "))
    if choice_3 == 1:
        print("You have selected Sedan")
    else:
        print("You have selected Hatchback")

elif (choice ==3):

    print("What type of bus?")
    print("1. Scania\n")
    print("2. Taxi\n")

    choice_4 = int(input("Enter your choice: "))
    if choice_4 == 1:
        print("You have selected Scania")
    else:
        print("You have selected Taxi")
else:
    print("Wrong Choice")