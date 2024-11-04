import random
def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to Triumph's Number Guessing Game(TNGG)!!")
    print("I'm thinking of a number between 1 and 100.")

    while not guessed:
        # Get user input
        try:
            guess = int(input("Enter your guess:"))
            attempts +- 1
            # Check if the guess is correct
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")

# Run the game
guess_the_number()