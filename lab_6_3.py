'''
За назвою місяця визначити відповідну пору року
Серебренніков Дмитро Олександрович група "В"
'''
while 'Rusakov'=='Rusakov':
    from enum import Enum
    class a(Enum):
        January=1
        February=2
        March=3
        April=4
        May=5
        June=6
        July=7
        August=8
        September=9
        October=10
        November=11
        December=12
    class b(Enum):
        Winter=1
        Spring=2
        Summer=3
        Autumn=4
    c=a[input('month:')]
    d=c.value
    if 3<=d<=5:
        print(b(2).name)
    if d<=2 or d==12:
        print(b(1).name)
    if 6<=d<=8:
        print(b(3).name)
    if 9<=d<=11:
        print(b(4).name)
