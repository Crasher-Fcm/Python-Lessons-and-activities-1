basket1 = {"Rice cakes", "Granola bars", "Doritos", "juice", "cheetos","cookies"}
basket2 = {"Cheese balls", "Apple slices", "Juice", "Cookies", "Gummy bears", "Doritos", "Fruit cups"}
print("Basket 1:", basket1)
print("Basket 2:", basket2)

basket1.add("Crackers")
print("Basket 1 after adding crackers:", basket1)

common_snacks = basket1.intersection(basket2)
print("Snacks in both baskets:", common_snacks)

import array as arr
snacks_counts = arr.array('i', [3,5,2,4,])
print("Snack counts array:", snacks_counts)

snacks_counts.insert(0,1)
snacks_counts.append(6)
print("Snack counts after adding items:", snacks_counts)

count_of_4 = snacks_counts.count(4)
print("Number of times 4 appears:", count_of_4)

print("Reversed snack counts array:", snacks_counts)

print("")
print("===== CLASS SNACK BASKET ORGANIZER =====")
print("Basket 1:", basket1)
print("Basket 2:", basket2)
print("Shared snacks:", common_snacks)
print("Snack counts:", snacks_counts)
print("==========================================")