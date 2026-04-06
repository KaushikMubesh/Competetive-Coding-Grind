def summer(n):
    if (n==0):
        return 0
    return n + summer(n-1)
print (summer(3))