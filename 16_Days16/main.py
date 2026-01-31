import menu
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 1 : Print Report
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

money_machine.report()
coffee_maker.report()

menu = Menu()


transaction = True
while transaction:
    options = menu.get_items()
    choice = input(f"What would you like? {options[:-1]} ?")

    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)

        coffee_maker = CoffeeMaker()

        # TODO 2 : Check resources sufficent ?
        if coffee_maker.is_resource_sufficient(drink):
            # TODO 3 : Process coins
            # TODO 4 : Check transaction successful ?
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)




