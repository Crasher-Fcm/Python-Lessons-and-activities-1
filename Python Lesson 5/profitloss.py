buying_price = float(input("Enter the actual cost of the item: "))

selling_price = float(input("Enter the selling price of the item: "))

if (selling_price > buying_price):
    profit = selling_price - buying_price
    print("You made a profit of: ", profit)
else:
    loss = buying_price - selling_price
    print("You incurred a loss of: ", loss)