a,b=eval(input('dati etajele:'))
if a<b:
    print(a)
    while a<b:
        a+=1
        print(a)

if a>b:
    print(a)
    while a>b:
        a-=1
        print(a)