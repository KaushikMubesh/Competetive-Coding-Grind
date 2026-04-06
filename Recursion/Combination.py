def Combination(arr,curr,i,target):
    if (i==len(arr)):
        print(curr)
        return 
    if(arr[i] <=target):
        curr.append(arr[i])
        Combination(arr,curr,i,target)
        curr.pop()
    Combination(arr,curr,i,target)

arr=[1,2,1,2,4,7,3]
target = 7
Combination(arr,[],0,target)