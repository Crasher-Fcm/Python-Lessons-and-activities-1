import random
import string

def generate_random_password(length=12):
    # Ensure the password contains at least one of each required type
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    
    # Combine all allowed characters for the remaining slots
    all_characters = string.ascii_letters + string.digits
    
    # Fill the rest of the password length randomly
    remaining_length = length - 3
    remaining_chars = [random.choice(all_characters) for _ in range(remaining_length)]
    
    # Combine all characters into a single list
    password_list = [lower, upper, digit] + remaining_chars
    
    # Shuffle the list to randomize character positions
    random.shuffle(password_list)
    
    # Join the list into a single string
    return "".join(password_list)

# Generate and print a 12-character random password
print("Generated Password:", generate_random_password(12))