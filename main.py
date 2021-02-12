from modules.menu import main_menu 
from modules import menu_validation
from modules import menu_options
from datetime import timedelta
from modules import movie
from modules import help_funcs



menu_option = 5


while menu_option != 4:
    help_funcs.clear_terminal()
    main_menu()
    option_selected = menu_validation.chose_a_option()
    menu_options.options(option_selected)
    if option_selected is 4:
        menu_option = option_selected 