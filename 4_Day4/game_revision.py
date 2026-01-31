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

if user_input < 0 or user_input > 2:
    print("Input salah! pilih angka 0, 1, atau 2")
else:
    user_choose = str(game[user_input])
    computer_choose = game[random.randint(0, 2)]

    print(f"kamu memilih {user_choose}")
    print(f"komputer memilih {computer_choose}")

    if user_choose == computer_choose:
        print("Coba lagi! pilihanmu sama dengan komputer")
    # Tanda \ setelah kata or dalam kode yang saya berikan sebelumnya berfungsi untuk memecah baris panjang menjadi dua baris, agar kode tersebut lebih mudah dibaca.
    elif (user_choose == "rock" and computer_choose == "scissors") or \
        (user_choose == "paper" and computer_choose == "rock") or \
        (user_choose == "scissors" and computer_choose == "paper"):
        print("Selamat, kamu menang!")
    else:
        print("mohon maaf anda kalah")
