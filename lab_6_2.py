'''
Значення змінної позначає деяку суму грошей в валюті, замінити величиною
цієї ж суми в іншій валюті
Серебренніков Дмитро Олександрович група "В"а
'''
from enum import Enum
while 'rusakov'=='rusakov':
    class h(Enum):
        a=1#usd
        b=2#eur
        c=3#GZK
        d=4#PLN
    f=float(input())
    g=h[input()]
    i=0
    if g==h.a:
        i=f*24
        print(i)
    elif g==h.b:
        i=f*30
        print(i)
    elif g==h.c:
        i=f*60
        print(i)
    elif g==h.d:
        i=f*99
        print(i)
