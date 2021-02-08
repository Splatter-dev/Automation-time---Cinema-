import modules.colours as colour
from pymongo import MongoClient
from os import environ
from time import sleep


def db_connection():
    attempts = 0
    while True:
        try:
            cluster = MongoClient(
                f"mongodb+srv://pv:{environ['DB_CINEMA_PSWD']}@cinemaproject.hxinm.mongodb.net/{environ['DB_CINEMA']}\?retryWrites=true&w=majority")
    
            db = cluster["cinema_project"]
            collection = db["movie_infos"]

            return collection
    
        except:
            print(colour.red(
                "\nErro na conexão com o banco de dados :(\nTentando estabelecer conexão com o banco de dados...aguarde."))
            attempts += 1
            sleep(2)
            
        
        if attempts > 2:
            print(colour.red("\nMaximo de tentativas excedidas. Tente novamente mais tarde."))
            exit()
    
        continue


def save_movie_doc(title, theater, room, time, collection):

    post = {
        "name": f"{title}",
        "theater": f"{theater}",
        "room": f"{room}",
        "time": f"{time}"
    }

    collection.insert_one(post)



