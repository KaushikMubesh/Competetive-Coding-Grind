def permu (arr,curr,b):

    if (len(curr)==len(arr)):
        print(curr)
        return 
    for i in range(0,len(arr)):
        if (b[i]!=1):
            curr.append(arr[i])
            b[i] = 1
            permu(arr,curr,b)
            b[i]=0
            curr.pop(-1)
        

arr=[1,2,3]
b=[0]*len(arr)
print(arr)
print(b)
permu(arr,[],b)
