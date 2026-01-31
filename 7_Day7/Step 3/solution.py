import random

word_list = ["coffee", "milk", "table", "mouse"]
nyawa = 10
game_over = False

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list).lower()
print(chosen_word)

# TODO 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
banyak_char = len(chosen_word)
print(f"Anda harus menebak kata yang mana hurufnya ada {banyak_char}")
tebak_kata = "_" * banyak_char



# letter = str([char for char in random_word]) # ini ga perlu sbnrnya cuman untuk belajar aja
# print(letter)

def tebak_letter(chosen_word, tebak_kata):
    tebak_letter = input("tebak letter of word dari random word nya ").lower()
    ditemukan = False  # flag awalnya blm ketemu
    tebak_kata_list = list(tebak_kata) # ubah string ke list supaya bisa dimodifikasi per indexs

    for index, letter in enumerate(chosen_word):
        if letter == tebak_letter:
            print(f"Right! Huruf '{tebak_letter}' ditemukan.")
            ditemukan = True
            tebak_kata_list[index] = tebak_letter

    updated_tebak_kata = "".join(tebak_kata_list)
    return  updated_tebak_kata, ditemukan

# panggil fungsi :
while not game_over:
    print("\n" + tebak_kata)
    tebak_kata, ditemukan = tebak_letter(chosen_word, tebak_kata)

    if ditemukan:
        print("Benar! Huruf tersebut ada di dalam kata.")
    else:
        nyawa -= 1
        print("Salah! Huruf tidak ditemukan.")
        print(f"Sisa nyawa kamu: {nyawa}")

    # Cek apakah pemain menang
    if "_" not in tebak_kata:
        print(f"\nSelamat! Kamu berhasil menebak kata: {chosen_word} ")
        game_over = True

    # Cek apakah pemain kalah
    if nyawa == 0:
        print(f"\nKamu kehabisan nyawa. Kata yang benar adalah: {chosen_word}")
        game_over = True



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