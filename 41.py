'''
Змінній t привласнити значення істина, якщо максимальний елемент
одновимірного масиву єдиний і не перевищує наперед заданого числа а.
Серебренніков Дмитро
'''
t=False
print('░░░░░░░░░░░░░░░░░░░░')
print('░░░░░░░░░░░░░░░░░░░░')
print('░░░░░░▄▀▀▀▄░░░░░░░░░')
print('▄███▀░◐░░░▌░░░░░░░░░')
print('░░░░▌░░░░░▐░░░░░░░░░')#просто гусь
print('░░░░▐░░░░░▐░░░░░░░░░')
print('░░░░▌░░░░░▐▄▄░░░░░░░')
print('░░░░▌░░░░▄▀▒▒▀▀▀▀▄')
print('░░░▐░░░░▐▒▒▒▒▒▒▒▒▀▀▄')
print('░░░▐░░░░▐▄▒▒▒▒▒▒▒▒▒▒▀▄')
print('░░░░▀▄░░░░▀▄▒▒▒▒▒▒▒▒▒▒▀▄')
print('░░░░░░▀▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▀▄')
print('░░░░░░░░░░░▌▌░▌▌░░░░░')
print('░░░░░░░░░░░▌▌░▌▌░░░░░')
print('░░░░░░░░░▄▄▌▌▄▌▌░░░░░')
a=int(input())#значение которое мы задаем чтобы его не привышала програ
d=-999#максимальный элемент
e=list()#
for b in range(10):#диапазон
    c=int(input())#ввод
    if c>d:#находим максимальное число
        d=c#
    e.append(c)#записуем абсолютно все элементы
f=(e.count(d))#количество максимальных
if f==1 and d<=a:#если количество макс элементов 1 и оно меньше заданого
    t=True#становится тру за условием
    print(t)#
