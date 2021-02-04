from datetime import timedelta
import platform
import os
from modules import help_funcs


begin = timedelta(seconds=15,minutes=12,hours=1)
end = timedelta(seconds=11,minutes=11,hours=1)
print(begin,end)

time_offset = begin - end

print(time_offset)


print((1-2))


print(platform.system())
print(os.name)



