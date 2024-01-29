import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        guess = int(input("Your guess: "))

        attempts += 1

        if guess < secret_number:
            print("Try a higher number.")
        elif guess > secret_number:
            print("Try a lower number.")
        else:
            print(f"Congratulations! You guessed the correct number, which is {secret_number}.")
            print(f"It took you {attempts} attempts.")
            break

while  True:
    number_guessing_game()
    d = input("Do you want to continue? if yes enter Y or y else Enter anykey: ") 
    if d == 'Y' or d == 'y':
        continue
    else:
        break