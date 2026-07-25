# 1) Create a class named `Parrot`.
class Parrot:
    # 2) Define a class attribute `species = "bird"`.
    #    (This attribute is shared by all objects of the class.)
    species = "bird"

# 3) Define the constructor method `__init__(self, name, age)`:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#    a) This method runs when a new object is created.
#    b) It takes two inputs: `name` and `age`.
coco = Parrot("Coco", 10)
Zazu = Parrot("Zazu", 7)
#    c) Store these values using instance attributes:
#       - `self.name = name`
#       - `self.age = age`
print("coco is a {0}".format(coco.species))
print("Zazu is also a {0}".format(Zazu.species))

# 4) Create (instantiate) two objects of the `Parrot` class:
#    a) `blu = Parrot("Blu", 10)`
#    b) `woo = Parrot("Woo", 15)`

# 5) Access and print the class attribute `species` using both objects:

#    a) Print that Blu is a bird.
#    b) Print that Woo is also a bird.

# 6) Access and print the instance attributes (`name` and `age`) for each object:
#    a) Print Blu’s name and age
print("{} is {} years old".format(coco.name, coco.age))
#    b) Print Woo’s name and age.
print("{} is {} years old".format(Zazu.name, Zazu.age))