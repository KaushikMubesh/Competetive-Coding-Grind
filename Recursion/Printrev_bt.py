def printer(x,n):
    if (x==n):
        return 
    printer (x+1,n)
    print(x)
printer(0,10)

