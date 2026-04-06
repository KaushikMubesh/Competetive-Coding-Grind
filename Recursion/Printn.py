def printer(n,val):
    if (n==val):
        return 
    else:
        print(n)
        printer(n+1,val)

printer(0,5)