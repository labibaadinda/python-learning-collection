# program requirements
# 1. print report : (it needs to be able to tell us what resources it has left,
#    how much water has left, how much milk etc
#    user ask report then it will print how much water has left, how much milk etc
# 2. check resources sufficient?
# 3. process coins
# 4. check transaction successful?
#    if they haven't inserted enough coins, refund and tell them "sorry.."
#    else: successful, then we're going to make the coffee
# 5. make a coffee

# Procedural Programming
# organizes programs as a series of step-by-step instructions, or procedures (also called
# routines or functions), that are called in a specific order.
# Procedural programming is a programming paradigm, classified as imperative programming,
# that involves implementing the behavior of a computer program as procedures
# (a.k.a. functions, subroutines) that call each other. The resulting program is a series of steps
# that forms a hierarchy of calls to its constituent procedures.

from data import MENU
from data import resources

# fungsi itu adalah kumpulan instruksi yang di kumpulin jadi satu
# buat fungsi aja agar lebih mudah manggil instruksi nya

# TODO: 1. Print report of all the coffee machine resources
# fungsi untuk mencetak laporan
def print_report():
    for key, value in resources.items():
        print(f"{key}: {value}")

# TODO: 2. Check is it sufficient resource or not
# fungsi untuk cek kecukupan bahan
def cek_kecukupan(menu, resouces):
    kurang = {}
    if menu not in MENU:
            print("Menu not found")

    for item, qty in MENU[menu]["ingredients"].items():
        # dictionary.get(key, default)
        # jadi didalam dict itu parameter nya key dan default
        # nah dari key itu bisa akses value dari key tersebut
        if resources.get(item, 0) < qty:
            kurang[item] = qty - resources.get(item, 0)

    return kurang if kurang else "cukup"

# TODO: 3. Process coins
# Fungsi untuk proses koin
def proses_koin():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = (quarters*0.25) + (dimes*0.10) + (nickels*0.05) + (pennies*0.01)
    return total

# Fungsi untuk cek transaksi
def cek_transaksi(total_uang, biaya):
    if total_uang < biaya:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        kembalian = total_uang - biaya
        if kembalian > 0:
            print(f"Here is ${round(kembalian, 2)} in change")
        return True

# Fungsi untuk mengurangi bahan
def kurangi_bahan(menu, resources):
    for item, qty in MENU[menu]["ingredients"].items():
        resources[item] -= qty
    print(f"Here is your {menu}. Enjoy !")


# TODO: 4. Check transaction is it successfull or not
transaction = True
while transaction:
    ask_menu = input("What would you like? (espresso/latte/cappuccino)")

    if ask_menu == "report":
        print_report()

    elif ask_menu == "off":
        transaction = False

    else:
        cek = cek_kecukupan(ask_menu, resources)
        if cek == "cukup":
            total_uang = proses_koin()
            biaya = MENU[ask_menu]["cost"]
            print(f"Total money inserted: ${total_uang}")

            if cek_transaksi(total_uang, biaya):
                kurangi_bahan(ask_menu, resources)
        else:
            print(f"The ingredients are not enough to make {ask_menu}. Ingredients which are not enough: {cek}")
# TODO: 5. Make a coffee
