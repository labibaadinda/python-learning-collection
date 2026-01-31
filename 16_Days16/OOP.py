# OOP (Object Oriented Programming) adalah paradigma pemrogramman yang mengorganisasi kode
# menjadi objek-objek yang berisi data (atribut) dan fungsi (metode) untuk melakukan tugas-tugas terterntu
# OOP ini fokusnya pada penggunaan "objek" - struktur data yang menggabungkan data dan fungsi.
# Jadi, daripada hanya menggunakan fungsi dan prosedur, OOP memungkinkan kita untuk mengelompokkan data
# dan perilaku dalam satu unit yang disebut objek

# OBJECT ATTRIBUTE

# atrribute itu adalah fancy word of variable yang mana ini terasosiasi dengan particular object, modeled by variable
# method itu adalah sesuatu yang dilakukan oleh object, modeled by function
# class itu blue print nya
# tiap object itu beda beda isi method dan attribute nya (walaupun few of cases same tp mostly bgt beda)
# contoh gampangnya manggil object di python : car = CarBluePrint()
#                                                        |
#                                                      Class
# nah kan kalo car itu dia objek ya misal di pakein attribute(fancy word of variable yang berasosiasi dengan objek)
# car dipakein attribute speed = 12
# car.speed (outoutnya = 12)
# kan mengaktifkan blue print nya itu dengan () itu the same way as activate the function
# tapi untuk oop itu disebut nya mengaktifkan construction gitu
# konstruktor itu adalah function yang berasosiasi dengan suatu object
# from another_module import another_variable

import another_module
print(another_module.another_variable)

# object di python : car = CarBluePrint()
#                               |
#                             Class



# import turtle
# timy = turtle.Turtle()

from turtle import Turtle, Screen
timy = Turtle()
print(timy)
timy.shape("turtle")
timy.color("DeepPink1")
timy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# OBJECT METHOD
# Function that are associated with that particular object
# and these function when it's tied to an object is known as METHOD
class CarBluePrint:
    # construction to initialize attributes
    def __init__(self):
        self.speed = 0
        self.fuel = 32
    #method
    def move(self):
        self.speed = 60
    def stop(self):
        self.speed = 0
# object can have things (attributes)
# object can do things (method)
# we call it a method because it's a function that a particular modeled object can do



car1 = CarBluePrint()
car1.stop()

car2 = CarBluePrint()
car2.move()
# Check the result
print(car1.speed)
print(car2.speed)

import prettytable
tabel = prettytable.PrettyTable()
tabel.field_names = ["no", "nama", "tanggal"]
tabel.add_row(["1", "labiba", "11"])
tabel.add_row(["2", "adinda", "12"])
tabel.add_row(["3", "zahwana", "13"])

# dst baca doc nya buat detailnya https://pypi.org/project/prettytable/
tabel.align = "l"
print(tabel)



