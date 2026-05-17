# Get input from user
char =input("Enter a Alphabet: ") 

# Check if the character is an alphabet
if char.isalpha():
    print(f"'{char}' is an alphabet.")
else:
    print(f"'{char}' is not an alphabet.")