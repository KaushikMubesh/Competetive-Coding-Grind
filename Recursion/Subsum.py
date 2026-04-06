def subsum(i,arr,l,n,su,t):
    if (i==n):
        if su==t:
            print(l)
        return
    l.append(arr[i])
    su+=arr[i]
    subsum(i+1,arr,l,n,su,t)
    su-=l[-1]
    l.pop()
    subsum(i+1,arr,l,n,su,t)

arr=[3,5,6,7]
subsum(0,arr,[],4,0,8)