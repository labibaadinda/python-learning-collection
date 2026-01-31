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
    tebak_kata = "_" * banyak_char
    print(tebak_kata)
else:
    print("yahhh anda salah, tebak sampai benar")




# letter = str([char for char in random_word]) # ini ga perlu sbnrnya cuman untuk belajar aja
# print(letter)
ditemukan = False # flag awalnya blm ketemu

if banyak_char == len_tebakan_user:
    tebak_letter = input("tebak letter of word dari random word nya ").lower()
    print(tebak_letter)

# ubah string ke list supaya bisa dimodifikasi per indexs
tebak_kata_list = list(tebak_kata)

for index, letter in enumerate(chosen_word):
    if letter == tebak_letter:
        print(f"Right! Huruf '{tebak_letter}' ditemukan.")
        ditemukan = True
        tebak_kata_list[index] = tebak_letter
    else:
        print("Wrong")


if ditemukan:
    print("Benar! Huruf tersebut ada di dalam kata.")
else:
    nyawa -= 1
    print("Salah! Huruf tidak ditemukan.")
    print(f"Sisa nyawa kamu: {nyawa}")

tebak_kata_fix = "".join(tebak_kata_list)
print(tebak_kata_fix)

# note
"""
kapan enumerate itu di pakai ?
- saat butuh index dan nilai secara bersamaan.
- misalnya lagi nyari posisi huruf tertentu dalam string / list.
- update elemen list berdasarkan posisi
- bikin permainan seperti tebak huruf (hangman style)
- cek posisi kesalahan dalam list / data
"""


# TODO 3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is True. Print "Wrong" if it is False.