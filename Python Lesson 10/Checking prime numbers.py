# Take two inputs from the user
lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

print("Prime numbers between", lower, "and", upper, "are:")
# Iterate loop from lower to upper limit
for num in range(lower, upper + 1):
    # Check if the number is greater than 1
    if num > 1:
        for i in range(2, num):
            # If the number is divisible by any number between 2 and num-1, it is not prime
            if (num % i) == 0:
                break
        else:
            print(num)