import modules.colours as colour
from modules import help_funcs
from time import sleep


def option_selected(option=""):
    while True:
        try:
            option_input = int(input(colour.purple("Digite uma opção: ")))
        except(ValueError, TypeError):
            print(colour.red("Digite um valor correto!"))
            # os.system("cls" if os.name == "nt" else 'clear')
            help_funcs.clear_terminal(3)
            break
        if option_input not in (1, 2, 3, 4):
            print(colour.red("Selecione uma opção valida!"))
            help_funcs.clear_terminal(3)
            break
        return option_input
