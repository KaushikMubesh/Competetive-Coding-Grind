def printer(n):
    if(n==0):
        return
    else:
        print(n)
        printer(n-1)

printer(10)