s='11'
n=7-2
y=""
def find(s,n,y):
    if(n==0):
        print(s)
        return 
    c=1
    for i in range(len(s)-1):
        if (s[i]!=s[i+1]):
            v=str(c)+str(s[i])
            y=y+v
            c=1
        else:
            c+=1
    v=str(c)+str(s[-1])
    y=y+v
    find(y,n-1,"")
find(s,n,"")
print(y)


