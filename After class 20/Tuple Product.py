def calculate_tuple_product(numbers_tuple):
    # Initialize the product to 1
    product = 1
    
    # Multiply each number in the tuple
    for number in numbers_tuple:
        product *= number
        
    return product

# Example usage:
example_tuple = (2, 9, 4, 5)
result = calculate_tuple_product(example_tuple)

print("The given tuple is:", example_tuple)
print("The product of all numbers is:", result)