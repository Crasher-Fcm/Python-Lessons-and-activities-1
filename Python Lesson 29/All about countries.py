# 1) Create a class `India` with three methods:
class India:
    def capital(self):
        print("Capital of India is New Delhi")

    def language(self):
        print("Main language spoken in India is Hindi")

    def type(self):
        print("India is a developing country")
#    a) `capital()` to print the capital of India.
#    b) `language()` to print the main language spoken in India.
#    c) `type()` to print the type of country India is.

# 2) Create another class `USA` with the same method names:
#    a) `capital()` to print the capital of USA.
#    b) `language()` to print the primary language of USA.
#    c) `type()` to print the type of country USA is.
class Usa():
    def capital(self):
        print("Washington, D.C. is the capital of USA")
    def language(self):
        print("English is the primary language of USA")
    def type(self):
        print("USA is a developed country")   

# 3) Create objects for both classes:
#    a) `obj_ind = India()`
#    b) `obj_usa = USA()`
obj_ind = India()
obj_usa = Usa()
# 4) Use a common interface (polymorphism) to call the same method names
#    on different objects:
#    a) Use a `for` loop to iterate through `(obj_ind, obj_usa)`.
#    b) For each object `country`, call:
#       - `country.capital()`
#       - `country.language()`
#       - `country.type()`
#    (Each object runs its own class implementation of these methods.)
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()