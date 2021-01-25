from modules.movie import Movie
from datetime import timedelta

# vingador = Movie("vingadores: A era de ultron", "polo", 4)
# mulher =  Movie("mulher maravilha 1984", "jaragua",2)
# tester =  Movie("1984", "jaragua",4)
# us =  Movie("Us", "jaragua",4)
# god = Movie("Godzilla: O mais fortes dos animais", "jaragua",4)


# print(vingador)
# print(mulher)
# print(tester)
# print(us)
# print(god)

begin = timedelta(seconds=15,minutes=12,hours=1)
end = timedelta(seconds=11,minutes=11,hours=1)


time_offset = begin - end


batman = Movie("vingadores: A era de ultron", "polo", 4, time_offset)
print(batman)