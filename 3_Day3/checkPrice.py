print("Selamat datang di rollercoster")
height = int(input("masukkan tinggi anda dalam cm : "))
bill = 0

if height >= 120:
    age = int(input("masukkan umur anda: "))
    if age <= 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12
    wants_photo = input("mau tambah fotonya ga? jawab y jika ya dan n jika tidak : ")
    if wants_photo == "y":
        bill += 3
    print(f"anda harus membayar sebesar ${bill}")
else:
    print("mohon maaf anda tidak bisa menaiki wahana ini")