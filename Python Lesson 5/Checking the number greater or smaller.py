number = int(input("Enter a number: "))

if (number < 15):
    print(number, "is smaller than 15")
    print("This is inside the if block")

else:
    print(number, "is greater than or equal to 15")
    print("This is inside the else block")
    
print("This is outside the if-else block")        