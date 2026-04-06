arr = [3,2,1]
n = len(arr)

for mask in range(1 << n):
    sub = []
    for i in range(n):
        if mask & (1 << i):
            sub.append(arr[i])
    print(sub)

