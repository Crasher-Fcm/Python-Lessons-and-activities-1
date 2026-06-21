def check_age():
    try:
        # Prompt the user to enter their age
        user_input = input("Please enter your age: ")
        
        # Try to convert the input into an integer
        age = int(user_input)
        
        # Validate that the age is a realistic positive number
        if age < 0 or age > 125:
            raise ValueError("Age must be between 0 and 125.")
            
        print(f"Age entered successfully: {age}")
        
        # Check if the age is even or odd
        if age % 2 == 0:
            print("The age entered is an EVEN number.")
        else:
            print("The age entered is an ODD number.")
            
    except ValueError as e:
        # Catch errors if input is not a number, or if it falls outside the valid range
        print(f"Error: Invalid age entered. ({e})")

# Run the program
if __name__ == "__main__":
    check_age()