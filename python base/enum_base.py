from enum import Enum
from enum import unique

# 方法一，生成Enum对象,默认的值从1开始

week = Enum("week", ("Mon", "Tue", "wed", "Thur", "Fri", "Sat", "Sun"))

print(type(week.Mon))


# 方法二，实现一个枚举类
@unique
class WeekDay(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


for name, member in WeekDay.__members__.items():
    print(name, "=>", member)
