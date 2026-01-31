try:
    age = int(input("How old are you? "))
except:
    print("You have typed in a an invalid number. Please try again with a numerical input")
    age = int(input("How old are you? "))

if age > 18:
    print(f"You can drive at age {age}")
else:
    print(f"You cannot drive at age {age}")

# == itu bukan asignment, itu tu buat ngecek true or false nya
# yang assignment itu adalah =