class IntegerToRoman:
    def __init__(self):
        # Map integer values to their corresponding Roman numeral symbols
        # Ordered from largest to smallest to facilitate the conversion logic
        self.val_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def convert(self, num: int) -> str:
        """Converts an integer value to a Roman numeral string."""
        roman_numeral = ""
        
        for value, symbol in self.val_map:
            # Determine how many times the current symbol fits into the number
            while num >= value:
                roman_numeral += symbol
                num -= value
                
        return roman_numeral

# --- Example Implementation ---
if __name__ == "__main__":
    # Instantiate the converter object
    converter = IntegerToRoman()
    
    # Test cases
    test_numbers = [3, 4, 9, 58, 1994, 2026]
    
    print("Integer to Roman Numeral Conversion:")
    print("-" * 36)
    for number in test_numbers:
        result = converter.convert(number)
        print(f"{number:<6} -> {result}")