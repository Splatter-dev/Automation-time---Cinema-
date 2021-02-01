import modules.colours as colour
import modules.menu_validation as validation
import modules.menu as menu
from time import sleep


def options(option_selected):
    if option_selected is 1:
        option_one()
    if option_selected is 4:
        option_four()


def option_one():
    menu.split_menu()
    print("\n")
    title = validation.name_input(title="")
    print(title)
    theater = validation.theater_option()
    print(theater)
    room = str(input(colour.purple("Qual foi a sala onde o filme foi testado: "))).strip().lower()

def option_two():
    pass


def option_three():
    pass


def option_four():
    print(colour.green(f"\nSaindo do programa...\nVolte sempre :)"))
