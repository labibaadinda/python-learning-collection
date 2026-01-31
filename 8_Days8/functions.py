# # Caesar Cipher
# # Functions with Inputs Arguments and Parameters
#
# def greet(y):
#     a = "hallo"
#     b = "iyaa"
#     c = "gmnmm"
#     print(a+b+c)
#
#
# greet()
#
# def life_in_weeks(current_age):
#     current_age_week = current_age * 52
#     week_90 = 90 * 52
#     weeks = week_90 - current_age_week
#     print(f"You have {weeks} weeks left.")
#
# life_in_weeks(12)
# def greet_with_location(name, lokasi):
#     print(f"hallo im {name}, im im from {lokasi}")
#     print(f"hello {name}")
#     print(f"What is it like in {lokasi}")
#
# greet_with_location(name="dinda", lokasi="bekasi")
#
#
# def calculate_love_score(name1, name2):
#     combine = (name1 + name2).lower()
#
#     letter_love = "LOVE".lower()
#     letter_true = "TRUE".lower()
#
#     love_score = 0
#     true_score = 0
#
#     for letter in letter_love:
#         love_score += combine.count(letter)
#
#     for letter in letter_true:
#         true_score += combine.count(letter)
#
#     final = int(str(true_score) + str(love_score))
#     print(final)
#
# 
# calculate_love_score("Kanye West", "Kim Kardashian")