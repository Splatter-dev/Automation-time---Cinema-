import modules.colours as colour
from modules import menu
from modules import help_funcs
from time import sleep


def chose_a_option(option=""):

    attempts = 0

    while True:
        if attempts >= 2:
            help_funcs.clear_terminal(2)
            menu.main_menu()
            attempts = 0

        try:
            option_input = int(input(colour.blue("Digite uma opção: ")))
        except(ValueError, TypeError):
            print(colour.red("Digite um valor correto!"))
            attempts += 1
            continue

        except(KeyboardInterrupt):
            print(colour.red("\nPrograma interrompido pelo usuario. Volte sempre :)"))
            exit()

        if option_input not in (1, 2, 3, 4):
            print(colour.red("Selecione uma opção valida!"))
            attempts += 1
            continue

        return option_input


def name_input(title):
    attempts = 0

    while True:

        if attempts >= 2:
            help_funcs.clear_terminal(2)

        try:
            title = str(
                input(colour.purple("Digite o nome do filme: "))).strip().lower()
        except(ValueError, TypeError):
            print(colour.red("Digite um valor correto!"))
            attempts += 1

        except(KeyboardInterrupt):
            print(colour.red("\nPrograma interrompido pelo usuario. Volte sempre :)"))
            exit()

        if title == "":
            print(colour.red("Digite um valor correto!"))
            attempts += 1
            continue

        if len(title) == 1:
            option = str(input(colour.purple("Você tem certeza que o nome é esse? [S/N] "))).strip().lower()

            if option == "s":
                return title
                break
            else:
                continue
   
        return title


def theater_option(theater_name=""):
    theaters = ("Polo", "Jarágua")

    while True:

        try:
            print(colour.purple("Escolha um dos complexos abaixo:"))
            print((colour.blue("1 - Polo\n2 - Jarágua")))
            chosen_option = int(input(colour.purple("\nDigite o número da opção:")))

        except(ValueError, TypeError):
            print(colour.red("Escolha uma das opções disponiveis usando o numero 1 ou 2!"))
            continue
        
        except(KeyboardInterrupt):
            print(colour.red("\nPrograma interrompido pelo usuario. Volte sempre :)"))
            exit()

        if chosen_option not in (1,2):
            print(colour.red("Opção indisponível. Escolha a opção 1 ou 2."))
            continue

        print(theaters[chosen_option - 1])
        return theaters[chosen_option - 1]


def room_options(theater):
    theater_rooms = (1,2,3,4) if theater.lower() == "jarágua" else (1,2,3,4,5)
    while True:
        try:
            room = int(input(colour.blue("Digite o número da sala em que o filme foi testado: ")))
            
        except(ValueError, TypeError):
            print(colour.red("Digite o número da sala!"))
            continue

        except(KeyboardInterrupt):
            print(colour.red("\nPrograma interrompido pelo usuario. Volte sempre :)"))
            exit()

        if room not in theater_rooms:
            print(colour.red(f"Temos apenas {theater_rooms[-1]} salas nesse cinema!"))
            continue

        return room