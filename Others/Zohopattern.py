n="12345"
e=0
for i in range(3):
    for j in range(e):
        print(" ",end="")
    e+=1
    print(n[0],end="")
    for j in range(len(n)-2):
        print(" ",end="")
    if (len(n)!=1):
        print(n[-1],end="")
    n=n[1:-1]
    print()