n=int(input('n='))
S1=0
S2=0
S3=0
S4=0
S5=0
S6=0
S7=0
P=1
i=1
while i<=n:
    S1+=i
    P*=i*(i+1)
    S2+=P
    P=1
    P*=i
    S3+=P
    S4+=(10*i)+2
    S5+=i/(i+2)
    S6+=(2*i)-((2*i)-1)
    S7+=20+i
    i+=1



print('S1=',S1)
print('S2=',S2)
print('S3=',S3)
print('S4=',S4)
print('S5=',S5)
print('S6=',S6)
print('S7=',S7)