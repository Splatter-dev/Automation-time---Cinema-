from modules.menu import main_menu 
from modules import menu_validation
from modules import menu_options
from datetime import timedelta
from modules import movie
from modules import help_funcs


# begin = timedelta(seconds=15,minutes=12,hours=1)
# end = timedelta(seconds=11,minutes=2,hours=0.1)


# time_offset = begin - end
# print(time_offset)

# teste = movie.Movie("","polo",4,12)
# print(teste)


menu_option = 5


while menu_option != 4:
    help_funcs.clear_terminal()
    main_menu()
    option_selected = menu_validation.chose_a_option()
    menu_options.options(option_selected)
    if option_selected is 4:
        menu_option = option_selected 