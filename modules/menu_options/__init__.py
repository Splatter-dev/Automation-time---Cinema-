import modules.colours as colour
import modules.menu_validation as validation
import modules.menu as menu
from time import sleep
from modules.movie import Movie, MovieFromDb
from db import db_connection



def options(option_selected):
    if option_selected is 1:
        option_one()
    if option_selected is 2:
        option_two()
    if option_selected is 3:
        option_three()
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

        movie = Movie(title,theater,room,time_offset)

        menu.split_menu()
        
        sleep(2)

        break

def option_two():

    documents = db_connection()

    menu.movies_registred()

    for dic in documents.find({}):
        movie = MovieFromDb(dic["name"], dic["theater"] ,dic["room"] ,dic["time"])
        print(movie)
    
    exit()


def option_three():

    documents = db_connection()

    title = validation.name_input(title="")

    find_document = documents.find_one({"name":f"{title}"},projection={"_id": False})

    movie = MovieFromDb(find_document["name"], find_document["theater"] ,find_document["room"] ,find_document["time"])

    menu.movies_registred()
    print(movie)

    exit()

def option_four():
    print(colour.green(f"\nSaindo do programa...\nVolte sempre :)"))
