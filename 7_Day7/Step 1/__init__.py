import random

word_list = ["coffee", "milk", "table", "mouse"]
nyawa = 10

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list).lower()
print(chosen_word)

# TODO 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
banyak_char = len(chosen_word)
print(banyak_char)
len_tebakan_user = int(input("tebak ada berapa huruf yang ada pada kata tersebut?"))
if banyak_char == len_tebakan_user:
    print("selamat anda benar")
else:
    print("yahhh anda salah, tebak sampai benar")

# letter = str([char for char in random_word]) # ini ga perlu sbnrnya cuman untuk belajar aja
# print(letter)
if banyak_char == len_tebakan_user:
    tebak_letter = input("tebak letter of word dari random word nya ").lower()
    print(tebak_letter)
    for letter in chosen_word:
        if letter == tebak_letter:
            print("Right")
        else:
            print("Wrong")


if letter == tebak_letter:
    print("Benar! Huruf tersebut ada di dalam kata.")
else:
    nyawa -= 1
    print("Salah! Huruf tidak ditemukan.")
    print(f"Sisa nyawa kamu: {nyawa}")



# TODO 3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is True. Print "Wrong" if it is False.