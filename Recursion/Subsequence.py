def subset(i,arr,d,n):
    if (i==n):
        print(d)
        return 
    d.append(arr[i])
    subset(i+1,arr,d,n)
    d.pop(-1)
    subset(i+1,arr,d,n)

arr=[3,2,1]
subset(0,arr,[],3)