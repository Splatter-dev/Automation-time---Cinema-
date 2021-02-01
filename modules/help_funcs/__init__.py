from os import system
from os import name
from time import sleep

def clear_terminal(sleep_time=0):
    sleep(sleep_time)
    system("cls" if name == "nt" else 'clear') 
    