#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

@unique
class Weekday(Enum):
	Sun = 0 # Sun的value被设定为0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

# 访问这些枚举类型可以有若干种方法：

day1 = Weekday.Mon
print(day1)
print(Weekday.Thu)
print(Weekday['Tue'])
print(Weekday.Tue.value)

print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)

print(Weekday(1))

print(day1 == Weekday(1))

# print(Weekday(7))

# 可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。