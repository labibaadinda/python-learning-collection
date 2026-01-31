student_score = [483, 639, 207, 542, 366, 125, 699, 310, 574, 448, 181, 502, 655, 394, 268, 107, 587, 326, 475, 613]

max_score = student_score[0]

for score in student_score:
    if score > max_score:
        max_score = score

print(max_score)
