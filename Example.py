'''2. Задача полягає у вивченні і реалізації алгоритмів пошуку для даних, підготовлених
за допомогою функції моделювання випадкових чисел і текстів, підготовлених
самостійно.
Для кожного алгоритму необхідно підготувати тести, що підтверджують
працездатність програми. Для всіх алгоритмів пошуку повинні бути приведені лістинги
програм пошуку та лістинги результатів (номера позиції в вихідному масиві, починаючи
з якого розташований елемент або фрагмент пошуку; кількості порівнянь по кожному
алгоритму пошуку).
Серебренников Дмитрий Александрович
'''



'''
Это так делать?
Или тут вообще всё неправильно?
Если правильно комментраии добавлю
'''


#1 Линейный
import numpy
import random
a=numpy.zeros(10,dtype=int)
b=5
for c in range(10):
    a[c]=random.randint(-5,5)
print(a)

d=len(a)
e=0
while e<d and a[e]!=b:
    e+=1

if e==d:
    print('Nothing')
else:
    print(f'Element - {b}; place - {e}')
#2 Бинарный
f=numpy.zeros(10,dtype=int)
g=4
for h in range(10):
    f[h]=random.randint(0,5)
print(f)
f=sorted(f)
i=0
j=len(f)-1
k=0
l=False
while i<=j and not l:
    k=(i+j)//2
    if f[k]==g:
        l=True
    elif f[k]<g:
        i=k+1
    else:
        j=k-1
if not l:
    print('Nothing')
else:
    print(f'Element - {g} place - {k}')
#3 Подстрока в строке
m='Тут шота написано'
n='шота написано'
o=-1
p=0
while (p<len(n)) and o<(len(m)-len(n)):
    p=0
    o+=1
    while p<len(n) and n[p]==m[p+o]:
        p+=1
if (p==len(n)):
    print(f'Substring is found {o}')
else:
    print('Nothing')






    
