books = ["The Great Gatsby", "1984", "To Kill a Mockingbird", "Brave New World", "The Lord of the Rings", "Harry Potter and the Sorcerer's Stone", "The Catcher in the Rye", "Pride and Prejudice", "The Hobbit", "Fahrenheit 451"]
stock_counts = [12, 7, 8, 5, 3, 9, 6, 4, 2, 1]

library = {item: count for item, count in zip(books, stock_counts)}
print("Full Inventory:", library)

in_stock_items = [item for item in books if library[item] > 0]
print("Items in stock:", in_stock_items)

chosen_item = input("What item would you like to buy? ")

if chosen_item not in library or library[chosen_item] == 0:
    print(chosen_item, "is out of stock! Stopping the checker")
    exit()

prices = [100, 80, 110, 10, 150, 195, 120, 35, 40, 45]
markup = int(input("Enter the markup amount to add to every price: "))


marked_up_prices = list(map(lambda p: p + markup, prices))
print("Marked up prices:", marked_up_prices)

item_index = books.index(chosen_item)
chosen_price = marked_up_prices[item_index]
print("The price of", chosen_item, "After markup is:", chosen_price)

library[chosen_item] = library[chosen_item] - 1
print(chosen_item, "purchased! Remaining stock:", library[chosen_item])

print("")
print("====== LIBRARY BOOK INVENTORY CHECKER ======")
print("Item Bought:", chosen_item)
print("Price Paid:", chosen_price)
print("Updated Library:", library)
print("=============================================")