alphabet = list('abcdefghijklmnopqrstuvwxyz')

direction = input("Type 'encode' to encrypt, type 'decode', to decrypt:\n").lower()
text = input("Type your message:\n").lower()
value = int(input("Type the shift number:\n"))

def caesar_cipher(text, shift, mode='encode'):
    result=''

    for letter in text:
        if letter in alphabet:
            old_index = alphabet.index(letter)
            if mode == 'encode':
                new_index = (old_index + shift) % 26
            else:
                new_index = (old_index - shift) % 26
            result += alphabet[new_index]
        else:
            result += letter
    return result

result = caesar_cipher(text, shift=value, mode=direction)
print(f"Hasil dari {direction} text adalah {result}")




