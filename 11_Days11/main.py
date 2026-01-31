"""
Blackjack Game House Rules
- The deck is unlimited in size
- There are no jokers
- The Jack/Queen/King all count as 10
- Use the following list as the deck of cards :
cards = [11, 2,3,4,5,6,7,8,9,10,10,10,10]
- The cards in the list have equal probability of being drawn
- Cards are not removed from the deck as they are drawn
- The computer is the dealer
"""
import random

still_playing = True
start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

# Deck kartu
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Inisialisasi hand
computer_cards = []
your_cards = []

# Fungsi untuk menghitung total nilai kartu
def calculate_hand(hand):
    total = sum(hand)

    # manangani kartu ace yang bisa bernilai 1 atau 11
    aces = hand.count(11)  # menghitung jumlah kartu ace (yang bernilai 11)
    # tidak bisa membuat Ace yang bernilai 1 sebanyak 11 kali dalam satu tangan.
    # Di dalam permainan Blackjack, Ace hanya bisa dihitung sebagai 1 atau 11, tetapi tidak lebih dari satu Ace yang dihitung sebagai 11 dalam satu tangan.


    # jika total lebih dari 21, ubah ace dari 11 menjadi 1 untuk mencegah bust
    while total > 21 and aces:
        total -= 10 # ubah ace dari 11 menjadi 1 (mengurangi 10 dari total)
        aces -= 1 # kurangi jumlah ace yang masih dihitung sebagai (total maksimal ambil nilai ace yang bernilai 1 itu hanya 11 maks nya)

    return total


if start == 'y':
    computer_cards.append(random.choice(cards))
    your_cards.append(random.choice(cards))
    while still_playing:

        print(f"Your cards: {your_cards}")
        print(f"Dealer cards: {computer_cards}")

        if sum(your_cards) > 21:
            print("You Lose!")
            still_playing = False
            break

        if sum(computer_cards) > 21:
            print("You Win!")
            still_playing = False
            break

        # main lagi
        play_again = input("Do you want to continue a game of Blackjack? Type 'y' or 'n': ")

        if play_again == 'y':
            # memberikan kartu lagi
            kamu = random.choice(cards)
            your_cards.append(kamu)
            comp = random.choice(cards)
            computer_cards.append(comp)
        else:
            # Pemain memilih berhenti, sekarang kita bandingkan skor akhir
            print(f"Final Your cards: {your_cards} (Total: {calculate_hand(your_cards)})")
            print(f"Final Dealer cards: {computer_cards} (Total: {calculate_hand(computer_cards)})")

            # cek siapa yang menang jika tidak ada yang bust
            if sum(your_cards) > 21:
                print("you lose!")
            elif sum(computer_cards) > 21:
                print("you win")
            else:
                if sum(your_cards) > sum(computer_cards):
                    print("You Win !")
                elif sum(your_cards) < sum(computer_cards):
                    print("You Lose !")
                else:
                    print("It's a tie !")
            still_playing = False  # Akhiri permainan setelah pengecekan

else:
    print("Thanks for playing!")





