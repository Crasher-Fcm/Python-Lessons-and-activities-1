class Pet:
    
    def _init_(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def display_profile(self):
        print("--- Pet Profile ---")
        print(f"Name:  {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Age:   {self.age} years old")
        print("-------------------\n")

pet1 = Pet("Buddy", "Golden Retriever", 3)
pet2 = Pet("Max", "German Shepherd", 5)

pet1.display_profile()