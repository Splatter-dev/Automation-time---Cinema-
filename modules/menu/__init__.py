import modules.colours as colour
from time import sleep


def main_menu():
    sleep(.5)
    split_menu()
    print("CINEMA - TIME OFFSET".center(60))
    split_menu()
    print(f"{colour.yellow('1')} - {colour.blue('Cadastrar novo filme')}")
    print(f"{colour.yellow('2')} - {colour.blue('Listar ultimos filmes cadastrados')}")
    print(f"{colour.yellow('3')} - {colour.blue('Pesquisar por filme cadastrado')}")
    print(f"{colour.yellow('4')} - {colour.blue('Sair do sistema')}")
    split_menu()


def split_menu(n=63):
    print("-" * n)


def movie_menu():
    split_menu()
    print("FILME".center(63))
    split_menu()


def theater_and_room_menu():
    split_menu()
    print("COMPLEXO E SALA".center(63))
    split_menu()


def time_calc_menu():
    split_menu()
    print("TEMPO RESTANTE OU CALCULO".center(63))
    split_menu()


def movies_registred():
    split_menu(63)
    print("FILMES CADASTRADOS".center(63))
    split_menu(63)
    print(f'{"Titulo":<28}{"Complexo"}{"Sala":>9}{"Time offset":^25}')
    split_menu(63)
