import modules.colours as colour
import modules.menu_validation as validation
import modules.menu as menu
from time import sleep
from modules.movie import Movie
from db import save_movie


def options(option_selected):
    if option_selected is 1:
        option_one()
    if option_selected is 4:
        option_four()


def option_one():
    while True:
        menu.movie_menu()
        title = validation.name_input(title="")

        menu.theater_and_room_menu()
        theater = validation.theater_option(theater_name="")
        room = validation.room_options(theater)

        menu.time_calc_menu()
        time_offset = validation.time_offset()

        save_movie.grava_no_banco(title,theater,room,time_offset)
        # movie = Movie(title,theater,room,time_offset)

        # print(movie)

        menu.split_menu()
        exit()

def option_two():
    pass


def option_three():
    pass


def option_four():
    print(colour.green(f"\nSaindo do programa...\nVolte sempre :)"))
