# Set the number of rows for the triangle
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    # Print leading spaces to push the stars to the right
    print(" " * (rows - i), end="")
    # Print the stars
    print("*" * i)