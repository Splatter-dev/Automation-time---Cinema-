from modules.movie import Movie
from modules.time import TimeOffset
from datetime import timedelta



begin = timedelta(seconds=15,minutes=12,hours=1)
end = timedelta(seconds=11,minutes=2,hours=1)


time_offset = begin - end
# print((time_offset))


us =  Movie("Us", "jaragua",1,time_offset)
god = Movie("Godzilla: O mais fortes dos animais", "jaragua",2,time_offset)
batman = Movie("vingadores: A era de ultron", "polo", 4, time_offset)
print(batman)
# print(us)
# print(god)