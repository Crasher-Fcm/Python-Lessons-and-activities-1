# Program to convert decimal to binary
decimal = int(input("Enter a decimal number: "))
binary = ""

if decimal == 0:
    binary = "0"
else:
    # Logic to convert decimal to binary
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2

print(f"The binary representation is: {binary}")