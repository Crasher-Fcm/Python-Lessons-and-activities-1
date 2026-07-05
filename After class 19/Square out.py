# Step 1: Get range boundaries from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Initialize empty lists to store the values
squares = []
odd_squares = []
even_squares = []

# Step 2: Generate the list of square values
for num in range(start, end + 1):
    squares.append(num**2)

# Step 3: Separate the squares into odd and even lists
for sq in squares:
    if sq % 2 == 0:
        even_squares.append(sq)
    else:
        odd_squares.append(sq)

# Step 4: Display the results
print("\n--- Results ---")
print(f"All squares in range: {squares}")
print(f"Odd squares:          {odd_squares}")
print(f"Even squares:         {even_squares}")