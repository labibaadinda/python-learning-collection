import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_extended = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
                    '±', '∞', '√', '≈', '≠', '∑', 'π', '∞', '÷', '×', '±', '§', '©', '®', '€', '£', '¥']

print("Welcome to the PyPassword Generator!")
nr_letter = int(input("Masukkan banyak nya huruf yang anda inginkan =  "))
nr_number = int(input("Masukkan banyak nya angka yang anda inginkan = "))
nr_symbol = int(input("Masukkan banyak nya simbol yang anda inginkan = "))

password_easy_level = ""
# password in easy level
for char in range(nr_letter):
    password_easy_level += random.choice(letter)

for char in range(nr_number):
    password_easy_level += random.choice(number)

for char in range(nr_symbol):
    password_easy_level += random.choice(symbols_extended)

print(f"Password ez anda adalah {password_easy_level}")

# hard level
password_hard_level = []
for char in range(nr_letter):
    password_hard_level.append(random.choice(letter))

for char in range(nr_number):
    password_hard_level.append(random.choice(number))

for char in range(nr_symbol):
    password_hard_level.append(random.choice(symbols_extended))

random.shuffle(password_hard_level)
password_hard = ""
for char in password_hard_level:
    password_hard += char
print(f"Password hard anda adalah {password_hard_level}")
print(f"Password hard anda adalah {password_hard}")

