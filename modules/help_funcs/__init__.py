from os import system
from os import name

def clear_terminal():
    system("cls" if name == "nt" else 'clear') 
    