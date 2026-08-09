class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You have borrowed '{self.title}' by {self.author}.")   
        else:
            print(f"Notice: '{self.title}' is already borrowed.") 

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"Success: '{self.title}' by {self.author} has been returned and is now available for purchasing.")     
        else:
            print(f"Notice: '{self.title}' was not borrowed.")


Book1 = Book("1984", "George Orwell")   
Book2 = Book("To Kill a Mockingbird", "Harper Lee")
Book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")        
Book4 = Book("Pride and Prejudice", "Jane Austen")

print("----- Testing borrow() method -----")
Book1.borrow()
Book2.borrow()
Book4.borrow()
Book3.borrow

print("\n----- Testing return_book() method -----")
Book1.return_book()
Book2.return_book()


print("\n --- Testing Edge Cases (Already Borrowed / Not Borrowed) ---")
Book2.borrow()
Book3.return_book()