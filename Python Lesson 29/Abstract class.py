# 1) Import `ABC` and `abstractmethod` from the `abc` module.
from abc import ABC, abstractmethod

#    (These are used to create abstract base classes in Python.)

# 2) Create an abstract base class named `Absclass` that inherits from `ABC`.
class Absclass(ABC):


# 3) Inside `Absclass`, define a normal method `print(self, x)`:
#    a) It takes a value `x` as input.
#    b) It prints the value passed to the method.
    def print(self, x):
        print("Passed Value: ", x)
# 4) Define an abstract method `task(self)` using the `@abstractmethod` decorator:
#    a) This method must be implemented (overridden) in any child class.
#    b) The print statement inside shows what the base version contains.
    @abstractmethod
    def task(self):
        print("We are inside abstract method task")

# 5) Create a subclass named `test_class` that inherits from `Absclass`.
class test_class(Absclass):

# 6) Implement the abstract method `task(self)` inside `test_class`:
#    a) Print "We are inside test_class task".
#    (This satisfies the abstract method requirement.)
    def task(self):
        print("We are inside test_class task")

# 7) Create an object `test_obj` of the class `test_class`.
#    (We can create this object because `task()` is implemented.)
test_obj = test_class()
test_obj.task()
test_obj.print(100)

# 8) Call `test_obj.task()` to run the overridden method in `test_class`.

# 9) Call `test_obj.print(100)` to print the value 100 using the parent class method.