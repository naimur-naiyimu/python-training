import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:
        # Generate a random number between 1 and 100 for each new game
        secret_number = random.randint(1, 100)
        attempts = 0

        while True:
            try:
                guess = int(input("Enter your guess, or enter -1 to quit: "))
                attempts += 1

                if guess == -1:
                    print(f"The secret number was {secret_number}. Better luck next time!")
                    break
                elif guess < 1 or guess > 100:
                    print("Your guess is out of range! Please guess between 1 and 100.")
                    continue
                elif guess < secret_number:
                    print("Too low! Try again.")
                elif guess > secret_number:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You've guessed the number {secret_number} correctly!")
                    print(f"It took you {attempts} attempts.")
                    break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break

guessing_game()
