import random
playing = True
number = (random.randint(0,9))

print("I will generate a number from 0 to 9, and you have to guess thenumber one digit at a time.")
while playing:
    guess = int(input("Enter your guess \n "))
    if number == guess:
        print("You win the game!")
        print("The number was", number)
        break
    else:
        print("You lose the game! Try again.")
        