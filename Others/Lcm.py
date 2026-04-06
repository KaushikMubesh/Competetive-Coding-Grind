c=0
def Lcm(x,n):
    g=1
    if (n>x):
        t=x
        x=n
        n=t
    global c
    while(True):
        if((x*g)%n==0):
            c+=x*g
            print(x*g)
            break
        g+=1
    return x*g

n=int(input())
s=0
for i in range(1,n+1):
    s+=Lcm(i,n)
print(s)