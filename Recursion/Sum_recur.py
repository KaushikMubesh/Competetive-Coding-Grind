def summer(i,n,s):
    s+=i
    if (n==0):
        print(s)
    else:
        summer(i+1,n-1,s)
print(summer(0,3,0)) 