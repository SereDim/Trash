'''
б) Задача. Вивести відомості про співробітників, у яких зарплата вище середньої і вік
менше 30-ти років. Поля структури: Прізвище, Посада, Зарплатня, Дата народження.
Серебренніков Дмитро В 15в
'''
g='Так'
p=0
while True:
    l={'Rusakov':'teacher','Nikoluk':'Cibersportsman'}#Jobs
    m={'Rusakov':14000, 'Nikoluk':7000}#Earings
    n={'Rusakov':20, 'Nikoluk':49}#Date of birth
    f=list(dict.values(m))
    y=list(l)
    j=len(m)
    for i in f:
        p=p+i
    u=p/j
    g=input('1, якщо бажаєте отримати результат')
    if g=='1':
            for k in f:
                if k>=u:
                    for o in dict.values(n):
                        if o<30:
                            print('Rusakov')
                            print(l['Rusakov'])
                            print(k)
                            print(o)
            break
