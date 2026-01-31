import random
rock = '''
    _______
__'  _____)
    (_____)
    (_____)
    (____)
__'__(___)
'''

paper = '''
___'------
    ___)___
        (_____)
    (____)
'''

scissors = '''
    (____)
----._________
    (____)
        (____)
        (____)
    (____)
----._________
    (____)
'''

game = ["rock", "paper", "scissors"]

user_input = int(input("kamu mau pilih apa? type 0 untuk batu (rock), 1 untuk kertas (paper), 2 untuk gunting (scissors) = "))
user_choose = str(game[user_input])
computer_choose = game[random.randint(0,2)]

if user_choose == "rock" and computer_choose == "scissors":
    print("congrats, you win!")
elif user_choose == "rock" and computer_choose == "paper":
    print("sorry, you lose!")
elif user_choose == "rock" and computer_choose == "rock":
    print("try again! you got the same chosen")
elif user_choose == "scissors" and computer_choose == "paper":
    print("congrats, you win!")
elif user_choose == "scissors" and computer_choose == "rock":
    print("sorry, you lose!")
elif user_choose == "scissors" and computer_choose == "scissors":
    print("try again! you got the same chosen")
elif user_choose == "paper" and computer_choose == "rock":
    print("congrats, you win!")
elif user_choose == "paper" and computer_choose == "scissors":
    print("sorry, you lose!")
elif user_choose == "paper" and computer_choose == "paper":
    print("try again! you got the same chosen")
else:
    print("you put the wrong number!")
