from abc import ABC, abstractmethod

# 1. Create an abstract class for a common smart device structure
class SmartDevice(ABC):
    def __init__(self, name):
        self.name = name

    # Define an abstract method to enforce abstraction
    @abstractmethod
    def activate(self):
        pass

    # Shared method name to be used polymorphically
    def status_report(self):
        print(f"Checking system status for {self.name}...")


# 2. Override methods in different device subclasses (Polymorphism)
class SmartLight(SmartDevice):
    def activate(self):
        return f"{self.name}: Lights turned ON. Brightness set to 100%."


class SmartThermostat(SmartDevice):
    def activate(self):
        return f"{self.name}: Thermostat activated. Temperature set to 22°C."


class SecurityCamera(SmartDevice):
    def activate(self):
        return f"{self.name}: Security Camera recording started."


# 3. Smart Device Command Center execution
if __name__ == "__main__":
    # Instantiate different devices
    devices = [
        SmartLight("Living Room Light"),
        SmartThermostat("Main Hall Thermostat"),
        SecurityCamera("Front Door Camera")
    ]

    print("--- Initializing Command Center ---")
    
    # Polymorphic execution loop
    for device in devices:
        device.status_report()    # Shared method inherited from parent
        print(device.activate())   # Polymorphic method overridden by child
        print("-" * 40)