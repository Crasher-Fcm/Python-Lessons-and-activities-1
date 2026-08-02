# 1) Create a class named `myClass`.
class myClass:
   
  

# 2) Inside the class, create a private class variable `__privateVar = 27`.
  
  __buscuit = 27;

#    (The double underscore makes it name-mangled, so it cannot be accessed directly outside the class.)
   

# 3) Define a private method `__privMeth(self)`:
  def __privMeth(self):
#    a) This method prints "I'm inside class myClass".
#    (It is also name-mangled because of the double underscore.)
    print("I'm inside class myClass")

# 4) Define a public method `hello(self)`:
  def hello(self):
#    a) Print the value of the private variable using `myClass.__privateVar`.
        print("Private variable value:", self.__buscuit)

# 5) Create an object `foo` of the class `myClass`.
foo = myClass()

# 6) Call the public method `foo.hello()` to display the private variable value.
foo.hello()

# 7) Attempt to access the private method using `foo.__privMeth`.
foo.__privMeth()
#    (This will not work directly because `__privMeth` is private/name-mangled.)