from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_running = True

machine = CoffeeMaker
current_menu = Menu
money_machine = MoneyMachine

while machine_running == True:
    machine_input = current_menu.find_drink(input('What would you like? (espresso/latte/cappuccino): '))

    if machine_input == 'off':
        print('Stopping Machine')
        machine_running = False
    elif machine_input == 'report':
        machine.report()
    else:
        if machine.is_resource_sufficient(machine_input) == True:
            if money_machine.make_payment(money_machine) == True:
                machine.make_coffee(current_menu.find_drink(machine_input))
