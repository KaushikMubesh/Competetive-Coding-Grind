s=2
n=12

area = s*s
k=0
for i in range(1,200):
    if (2**i>n):
        k=2**(i-1)
        break
print(area*k)