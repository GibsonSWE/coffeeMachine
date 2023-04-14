from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
current_menu = Menu()
money_module = MoneyMachine()

machine_running = True
while machine_running:
    machine_input = input(f'What would you like? ({current_menu.get_items()}): ')

    if machine_input == 'off':
        print('Stopping Machine')
        machine_running = False
    elif machine_input == 'report':
        money_module.report()
        machine.report()
    else:
        drink = current_menu.find_drink(machine_input)
        if machine.is_resource_sufficient(drink):
            if money_module.make_payment(drink.cost):
                machine.make_coffee(drink)
