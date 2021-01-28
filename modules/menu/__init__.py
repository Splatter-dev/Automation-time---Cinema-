import modules.colours as colour
from time import sleep


def main_menu():
    sleep(.5)
    print("-"*60)
    print("CINEMA - TIME OFFSET".center(60))
    print("-"*60)
    print(f"{colour.yellow('1')} - {colour.blue('Cadastrar novo filme')}")
    print(f"{colour.yellow('2')} - {colour.blue('Listar ultimos filmes cadastrados')}")
    print(f"{colour.yellow('3')} - {colour.blue('Pesquisar por filme cadastrado')}")
    print(f"{colour.yellow('4')} - {colour.blue('Sair do sistema')}")
    print("-"*60)



