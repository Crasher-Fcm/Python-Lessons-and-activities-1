items = ["Pencils", "Notebooks", "Erasers", "Sharpener", "Markers", "Glue sticks"]
stock_counts = [12, 0, 8, 5, 3, 9]

inventory = {item: count for item, count in zip(items, stock_counts)}
print("Full Inventory:", inventory)

in_stock_items = [item for item in items if inventory[item] > 0]
print("Items in stock:", in_stock_items)

chosen_item = input("What item would you like to buy? ")

if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(chosen_item, "is out of stock! Stopping the checker")
    exit()

prices = [40, 80, 5, 10, 15, 25]
markup = int(input("Enter the markup amount to add to every price: "))


marked_up_prices = list(map(lambda p: p + markup, prices))
print("Marked up prices:", marked_up_prices)

item_index = items.index(chosen_item)
chosen_price = marked_up_prices[item_index]
print("The price of", chosen_item, "After markup is:", chosen_price)

inventory[chosen_item] = inventory[chosen_item] - 1
print(chosen_item, "purchased! Remaining stock:", inventory[chosen_item])

print("")
print("====== SCHOOL STORE INVENTORY CHECKER ======")
print("item Bought", chosen_item)
print("Price Paid:", chosen_price)
print("Updated Inventory:", inventory)
print("=============================================")