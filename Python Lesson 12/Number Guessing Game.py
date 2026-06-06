# input number to guess
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 50.")
secret_number = 25  # You can change this to any number between 1 and 50
lives = 5
number_to_guess = int(input("Enter your guess: "))  # between 1 and 50

# check if the guess is correct
while lives > 0:
    # display lives as heart emojis
    print("Lives: " + "❤️ " * lives)

    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess == secret_number:
        print("Congratulations! You guessed the number!")
        won = True
        break

    diff = abs(secret_number - guess)

    if diff >= 20:
        print("Hint: Ice Cold ❄️")
    elif diff <= 10:
        print("Hint: cold 🥶")
    elif diff <= 5:
        print("Hint: Warm 🔥")
    else:
        print("Hint: Hot 🔥🔥")

lives -= 1
print("Wrong guess! Try again.")

if not won:
    print("Game Over! You've used all your lives.")
    print(f"The number was {secret_number}.")