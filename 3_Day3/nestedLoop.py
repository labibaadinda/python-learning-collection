height = int(input("What is your height in cm? "))
bill = 0


if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child need to pay $5 to ride")
    elif age >= 12 and age <= 18:
        bill = 7
        print("Youth need to pay $7 to ride")
    else:
        bill = 12
        print("Adult need to pay $12")

    wants_photo = input("Do you want a photo to take? TYPE 'y' for Yes and 'n' for No ")
    wants_photo.lower()
    if wants_photo == 'y':
        bill = bill + 3
        print(f"You need to pay ${bill}, there's adding $3")
    else:
        print(f"You need to pay {bill}")

else:
    print("sorry, you can't ride")