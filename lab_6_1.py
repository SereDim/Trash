'''За датою визначити дату наступного і попереднього дня. Програмі врахувати
наявність високосних днів
Серебренніков Дмитро Олександрович група "В"
'''
while 'Rusakov'=='Rusakov':
    d=int(input('d'))
    e=int(input('m'))
    f=int(input('y'))
    g=['RUSAKOV',list(range(1,32)),#January
       list(range(0,29)),#February
       list(range(0,32)),#March
       list(range(0,31)),#April
       list(range(0,32)),#May
       list(range(0,31)),#June
       list(range(0,32)),#July
       list(range(0,32)),#August
       list(range(0,31)),#September
       list(range(0,32)),#October
       list(range(0,31)),#November
       list(range(0,32)),#December
       list(range(0,30)),#fkn.February
       ]
    if f%4==0:
        g[2]=g[13]
    if e>12 or e==0:
        print('RUSAKOV')
    h=(g[e])
    i=max(h)
    j=min(h)
    m=e#mnt
    n=f#yer
    k=d+1
    if k>i:
        if e==12:
            f+=1
            e=1
            k=1
        else:
            e+=1
            k=1
    print('next day:'+ str(k))
    print('month:'+ str(e))
    print('year:'+ str(f))

    h=(g[e-1])
    l=d-1
    if l==0:
        if m==1:
            n=-1
            m=12
            l=max(h)
        else:
            m-=1
            l=max(h)
    print('last day:'+ str(l))
    print('month:'+ str(m))
    print('year:'+ str(n))
