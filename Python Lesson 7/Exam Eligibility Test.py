# Take input for the student that he can attend the exam or not
medical_cause = input("Did you have a medical cause? (Y/N): ").strip().upper()

# Checking the user input and predicting output accordingly
if medical_cause == 'Y':  # Condition 1
    print("You are allowed to write the exam")
else:
    # Take input of the attendance
    attend = int(input("Enter the attendance of the student: "))   

    if attend >= 75:  # Condition 2
       print("Allowed")

    else:  
       print("Not allowed")  