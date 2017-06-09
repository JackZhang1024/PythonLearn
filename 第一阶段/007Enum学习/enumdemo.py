#-*- coding:utf-8 -*-
from enum import Enum,unique
class Weekdays(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
print(Weekdays.Sun)
print(Weekdays.Sat)
print(Weekdays(1))
for name,member in Weekdays.__members__.items():
    print(name,"=>",member)
	
Month=Enum('MONTH',('Jan','Feb','Mar'))
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)
