class Car():
    def __init__(self):
        self.seats = 5

    def enter_race_mode(self):
        self.seats = 2


user1 = Car()
print(f"default value seats: {user1.seats}")

user1.enter_race_mode()
print(f"saat dia menggunakan method race mode (biar mobilnya cepet kan seatnya di kurangin, tadinya 5 jadi 2), nah seats mmobil user1 menjadi: {user1.seats}")