from modules.menu import main_menu 
from modules import menu_validation
from modules import menu_options
from datetime import timedelta



# begin = timedelta(seconds=15,minutes=12,hours=1)
# end = timedelta(seconds=11,minutes=2,hours=1)


# time_offset = begin - end
# print(time_offset)


menu_option = 5


while menu_option != 4:
    main_menu()
    option_selected = menu_validation.option_selected()
    menu_options.options(option_selected)
    if option_selected is 4:
        menu_option = option_selected 