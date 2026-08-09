# 1. Define the parent Vehicle class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Vehicle: {self.make} {self.model}"


# 2. Build a child Bus class inheriting from Vehicle
class Bus(Vehicle):
    def __init__(self, make, model, capacity):
        # Use super() to inherit parent features
        super().__init__(make, model)
        self.capacity = capacity

    # Override a method from the parent class
    def display_info(self):
        return f"Bus: {self.make} {self.model} (Capacity: {self.capacity} passengers)"


# --- Verification and Testing ---

# Create instances to verify functionality
generic_vehicle = Vehicle("Toyota", "Corolla")
school_bus = Bus("International", "School Bus 305", 50)

print(generic_vehicle.display_info())
print(school_bus.display_info())

# 3. Check the inheritance relationship with issubclass()
is_child = issubclass(Bus, Vehicle)
print(f"\nIs Bus a subclass of Vehicle? {is_child}")