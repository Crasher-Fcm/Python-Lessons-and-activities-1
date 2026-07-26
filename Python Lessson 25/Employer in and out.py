# 1) Create a class named `Employee`.
class Employee:

# 2) Define the constructor method `__init__(self)`:
    def __init__(self):
#    a) This method runs automatically when an object is created.
#    b) Print "Employee created" to show the object has been initialized.
        print("Employee created")

# 3) Define the destructor method `__del__(self)`:
    def __del__(self):
#    a) This method runs automatically when the object is destroyed (removed from memory).
#    b) Print "Destructor called" to show the destructor is executed.
        print("Destructor called")

# 4) Define a function `Create_obj()` to create and return an object:
def Create_obj():

#    a) Print "Making Object..."
    print("Making Object...")
#    b) Create an `Employee` object and store it in `obj`.
    obj = Employee()
#    c) Print "function end..."
    print("function end...")
#    d) Return the object `obj`.
    return obj

# 5) Print "Calling Create_obj() function..." before calling the function.
print("Calling Create_obj() function...")

# 6) Call `Create_obj()` and store the returned object in `obj`.
obj = Create_obj()

# 7) Print "Program End..." to indicate the program is finishing.
#    (When the program ends, Python may call the destructor automatically.)
print("Program End...")