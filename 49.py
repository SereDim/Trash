'''
Задано дві таблиці. Одна містить найменування послуг, а інша - розцінки
за ці послуги. Видаліть з обох таблиць все, що передує послузі, ціна якої G гривень.
Серебренніков Дмитро
'''
a=['aaa','bbb','ccc','ddd']#первый массив
b=[14,1645,456345,45365634563456]#второй массив
c=int(input())#цена товара который нужно удалить
for d in range(len(b)):диапазон
    try:#так как в цыкле все будет идти к 4, а размер при
        if b[d]==c:#соблюдении условие становится 3, то выдает ошибку,
            a.remove(a[d])#я решил через трай сделать
            b.remove(b[d])#без понятия как по-другому сделать
    except:#
        break#
print(a)#
print(b)#
