import random

logo = """
 ________                               _______               ___.                 
 /  _____/ __ __   ____   ______ ______  \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/  /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/          \/            \/    \/     \/       
"""
print("Welcome to the Number Guessing Game!")
print("Im thinking of a number between 1 and 100")
level = str(input("Choose a difficulty. Type 'easy' or 'hard': ")).strip()
if level == 'easy':
    attempts = 10
elif level == 'hard':
    attempts = 5
else:
    print("Invalid input. Please choose 'easy' or 'hard'. ")
    exit()

computer_number = random.randint(1, 100)
still_playing = True

while still_playing and attempts > 0:
    print(f"You have {attempts} remaining to guess the number")

    try:
        guess_number = int(input("Make a guess : "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess_number == computer_number:
        print(logo)
        print(f"Congratulation you got it ! The answer was {computer_number}.")
        exit()
    elif guess_number > computer_number:
        print("Too high")
    elif guess_number < computer_number:
        print("Too low")

    attempts -= 1

    # if no attempts remain
    if attempts == 0:
        print(f"You lose! the answer was {computer_number}")
        still_playing = False




