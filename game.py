import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guess = None

    while guess != secret_number:
        # Get user's guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Increase attempt count
        attempts += 1

        # Check the guess
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
