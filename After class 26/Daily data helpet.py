class DailyDataHelper:
    def __init__(self, data_list=None):
        """Constructor to set default values."""
        if data_list is None:
            self.data_list = []
        else:
            self.data_list = data_list
        print("Daily Data Helper initialized with data.")

    def search_data(self):
        """Uses enumerate() to search through values with index numbers and data values."""
        if not self.data_list:
            print("No data available to search.")
            return

        print("\n--- Searching Through Daily Data ---")
        # enumerate() provides both the index and the item value
        for index, value in enumerate(self.data_list):
            print(f"Index {index}: Data Value -> {value}")

    def __del__(self):
        """Destructor to show when an object ends."""
        print("Daily Data Helper object destroyed. Process completed.")


# --- Testing the Object-Oriented Program ---
if __name__ == "__main__":
    # 1. Create dummy daily data values
    sample_data = ["Steps: 8500", "Water: 2.5L", "Sleep: 7.5hrs", "Calories: 2100"]

    # 2. Instantiate the class (triggers __init__)
    helper = DailyDataHelper(sample_data)

    # 3. Call the method that uses enumerate()
    helper.search_data()

    # 4. Explicitly delete the object or let the script end (triggers __del__)
    del helper