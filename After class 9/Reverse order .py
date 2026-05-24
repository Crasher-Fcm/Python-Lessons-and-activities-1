# Get input from the user
num = int(input("Enter a number: "))
count = 0

# Handle the case where the number is 0
if num == 0:
    count = 1
else:
    # Use absolute value to handle negative numbers
    num = abs(num)
    while num > 0:
        num //= 10  # Integer division to remove the last digit
        count += 1

print(f"Total digits: {count}")