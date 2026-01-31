import logo
from game_data import data
import random

right = True
score = 0
right_answer = ""

def higher_lower_guess():
    random1 = random.choice(data)
    random2 = random.choice(data)
    return random1, random2

while right:
    higher_lower_guess()
    random1, random2 = higher_lower_guess()
    # display logo art
    print(logo.logo)
    print(f"Compare A {random1['name']}, {random1['description']}, {random1['country']}")
    print(logo.vs)
    print(f"Againts B {random2['name']}, {random2['description']}, {random2['country']}")

    user_answer = str(input("Who has higher follower? ").strip().lower())
    if random1['follower_count'] > random2['follower_count']:
        right_answer = 'a'
    elif random2['follower_count'] > random1['follower_count']:
        right_answer = 'b'
    else:
        print("The value is same try again")

    if user_answer == right_answer:
        score += 1
    else:
        print("\n"*20)
        print(logo.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        right = False








