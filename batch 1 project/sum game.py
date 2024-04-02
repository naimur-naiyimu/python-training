import random
import time

def generate_numbers(limit):
    num1 = random.randint(1, limit)
    num2 = random.randint(1, limit)
    return num1, num2

def play_game(time_limit, level):
    num1, num2 = generate_numbers(level*20)
    print("Add the following two numbers:")
    print(num1, "+", num2)

    start_time = time.time()
    user_input = input("Enter the sum: ")

    if time.time() - start_time > time_limit:
        print("Time's up! You lose!")
        return False

    try:
        user_sum = int(user_input)
    except ValueError:
        print("Invalid input! Please enter a number.")
        return False

    if user_sum == num1 + num2:
        print("Correct!")
        return True
    else:
        print("Incorrect! The correct sum was:", num1 + num2)
        return False


level = 1
time_limit = 30

while True:
    print("Level", level)
    if play_game(time_limit,level):
        if level == 5:
            print("Congratulations! You've completed all levels!")
            break
        level += 1
        time_limit -= 5
        print("You've advanced to the next level with a time limit of", time_limit, "seconds.")
    else:
        print("Game over! Try again.")
        break
 