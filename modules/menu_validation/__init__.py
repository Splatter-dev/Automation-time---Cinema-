import modules.colours as colour
from modules import menu
from modules import help_funcs
from time import sleep


def option_selected(option=""):

    attempts = 0

    while True:
        if attempts >= 2:
            help_funcs.clear_terminal(2)
            menu.main_menu()
            attempts = 0

        try:
            option_input = int(input(colour.purple("Digite uma opção: ")))
        except(ValueError, TypeError):
            print(colour.red("Digite um valor correto!"))
            attempts += 1
            continue

        if option_input not in (1, 2, 3, 4):
            print(colour.red("Selecione uma opção valida!"))
            attempts += 1 
            continue

        return option_input
