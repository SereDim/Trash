'''
Дан одновимірний масив а. Сформувати новий масив, який складається
тільки з тих елементів масиву а, які перевищують свій номер на 10. Якщо таких
елементів немає, то видати повідомлення.
Серебренніков Дмитро
'''
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]#
b=a[10:]#вырезаем 10 невинных циферок

#卐

if b==[]:#Если элементов нет, то это будет пустой список
    print('Видаю повідомлення')#
else:#в противоположном случае выдаем результат
    print(b)#
