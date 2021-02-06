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

    while True:

        try:
            title = str(
                input(colour.purple("Digite o nome do filme: "))).strip().lower()
        except(ValueError, TypeError):
            print(colour.red("Digite um valor correto!"))

        except(KeyboardInterrupt):
            print(colour.red("\nPrograma interrompido pelo usuario. Volte sempre :)"))
            exit()

        if title == "":
            print(colour.red("Digite um valor correto!"))
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
            chosen_option = int(input(colour.purple("\nDigite o número da opção: ")))

        except(ValueError, TypeError):
            print(colour.red("Escolha uma das opções disponiveis usando o numero 1 ou 2!"))
            continue
        
        except(KeyboardInterrupt):
            print(colour.red("\nPrograma interrompido pelo usuario. Volte sempre :)"))
            exit()

        if chosen_option not in (1,2):
            print(colour.red("Opção indisponível. Escolha a opção 1 ou 2."))
            continue

        return theaters[chosen_option - 1]


def room_options(theater):
    theater_rooms = (1,2,3,4) if theater.lower() == "jarágua" else (1,2,3,4,5)
    while True:
        try:
            room = int(input(colour.purple("Digite o número da sala em que o filme foi testado: ")))
            
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


def time_offset():
        while True:

            try:
                print(colour.purple("Escolha uma das opções abaixo:"))
                print((colour.blue("1 - O tempo restante para acabar o filme")))
                print((colour.blue("2 - Calcular o tempo restante para acabar o filme")))
                chosen_option = int(input(colour.purple("\nDigite o número da opção: ")))

            except(ValueError, TypeError):
                print(colour.red("Escolha uma das opções disponiveis usando o numero 1 ou 2!"))
                continue
            
            except(KeyboardInterrupt):
                print(colour.red("\nPrograma interrompido pelo usuario. Volte sempre :)"))
                exit()

            if chosen_option not in (1,2):
                print(colour.red("Opção indisponível. Escolha a opção 1 ou 2."))
                continue

            if chosen_option == 1:
                menu.split_menu()
                print(colour.purple("Digite o tempo restante do filme.\n"))
                remaining_time = evaluate_time(end_time="")

            if chosen_option == 2:
                menu.split_menu()

                print(colour.purple("Digite o tempo total da playlist."))
                playlist_duration = evaluate_time(time="")
                

                print(colour.purple("\nDigite o tempo decorrido da playlist."))
                playlit_elapsed_time = evaluate_time(time="") 

                print(playlist_duration)
                print(playlit_elapsed_time)

                remaining_time = calc_remaining_time(playlist_duration, playlit_elapsed_time)
                

            return(remaining_time)


def evaluate_time(time):
    print("passou aqui")
    hour = verification_hour(hour_to_verify="")
    minutes = verification_minutes_or_seconds(minutes_or_seconds_to_verify="",msg="Minutos: ")
    seconds = verification_minutes_or_seconds(minutes_or_seconds_to_verify="", msg="Segundos: ")

    return (hour, minutes, seconds)


def verification_hour(hour_to_verify="",msg=""):
    while True:
        try:
            hour =  str(input(colour.yellow('Hora: '))).strip()

        except(ValueError, TypeError):
            print(colour.red("Digite um valor correto! Exemplo: 01 \n"))
            continue

        if not hour.isnumeric():
            print(colour.red("Digite um valor correto! Exemplo: 01"))
            continue

        if len(hour) > 2:
            print(colour.red("Digite um valor correto! Exemplo: 01"))
            continue
        
        return int(hour[-1])
        


def verification_minutes_or_seconds(minutes_or_seconds_to_verify="",msg=""):
    while True:
        try:
            minutes_or_seconds =  str(input(colour.yellow(f'{msg}'))).strip()

        except(ValueError, TypeError):
            print(colour.red("Digite um valor correto! Exemplo: 09 ou 10 \n"))
            continue

        if not minutes_or_seconds.isnumeric():
            print(colour.red("Digite um valor correto! Exemplo: 09 ou 10"))
            continue

        if len(minutes_or_seconds) > 2:
            print(colour.red("Digite um valor correto! Exemplo: 09 ou 10"))
            continue
        
        minutes_or_seconds = minutes_or_seconds[1] if minutes_or_seconds[0] == "0" else minutes_or_seconds

        return int(minutes_or_seconds)


def calc_remaining_time(playlist_duration, playlit_elapsed_time):

    h_duration , m_duration, s_duration = playlist_duration


    h_elapsed, m_elapsed, s_elapsed = playlit_elapsed_time
