    print("Select your type of ride")
    print("1.  Bike")
    print("2.  Car")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("What type of bike?")
        print("1. Sports Bike\n")
        print("2. Cruiser Bike\n")

        choice_2 = int(input("Enter your choice"))
        if choice_2 == 1:
           print("You have selected Sports Bike")
        else:
           print("You have selected Cruiser Bike") 

    elif (choice == 2):   

        print("What type of car?")   
        print("1. Mercedes\n") 
        print("2. Sedan\n")

        choice_3 = int(input("Enter your choice"))
        if choice_3 == 1:
            print("You have selected Mercedes")
        else:
            print("You have selected Sedan")
    else:
        print("Wrong Choice")    




       
