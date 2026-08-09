class AccountPinChecker:
    def __init__(self, initial_pin):
        """Initializes the account with a private PIN attribute."""
        # The double underscore makes the attribute private
        self.__pin = None  
        self.set_pin(initial_pin)

    def get_pin(self):
        """Getter method to view the current PIN."""
        return self.__pin

    def set_pin(self, new_pin):
        """Setter method to validate and update the PIN safely."""
        # Convert to string to easily check length and digits
        pin_str = str(new_pin)
        
        # Validation rules: Must be exactly 4 digits long and all numbers
        if len(pin_str) == 4 and pin_str.isdigit():
            self.__pin = pin_str
            print("PIN updated successfully.")
        else:
            print("Error: PIN must be exactly 4 numeric digits. PIN not changed.")

    def __str__(self):
        """Special function controlling how the object is displayed with print()."""
        if self.__pin:
            # Mask the first two digits for safety (e.g., "**34")
            masked_pin = "**" + self.__pin[2:]
            return f"Account Status: Secure | PIN: {masked_pin}"
        else:
            return "Account Status: Unsecured | No valid PIN set."


# --- Test Cases to Demonstrate Functionality ---
if __name__ == "__main__":
    print("--- Creating account with a valid 4-digit PIN (1234) ---")
    my_account = AccountPinChecker(1234)
    print(my_account)  # Triggers the __str__ method
    
    print("\n--- Trying to change PIN to an invalid length (123) ---")
    my_account.set_pin(123)
    print(my_account)
    
    print("\n--- Trying to change PIN to non-numeric characters (12a4) ---")
    my_account.set_pin("12a4")
    print(my_account)
    
    print("\n--- Testing private attribute protection from outside the class ---")
    try:
        # This will fail because __pin is private and encapsulated
        print(my_account.__pin)
    except AttributeError:
        print("Success: Cannot access '__pin' directly from outside the class!")
        
    print("\n--- Updating with a new valid PIN (5678) ---")
    my_account.set_pin(5678)
    print(my_account)