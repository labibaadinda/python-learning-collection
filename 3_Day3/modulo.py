# modulo menampilkan hasil sisa dari operasi
# 10 % 5 = 0, 0 is remainder
# 9 % 5 = 4, 4 is remainder
# modulo itu sisa pembagiannya

# contoh cek apakah bilangan genap atau bukan

angka = int(input("Input angka yang ingin di cek? "))

if angka % 2 == 0:
    print("angka tersebut adalah bilangan genap.")
elif angka % 2 == 1:
    print("angka tersebut adalah bilangan ganjil")
else:
    print("format nya salah!")
