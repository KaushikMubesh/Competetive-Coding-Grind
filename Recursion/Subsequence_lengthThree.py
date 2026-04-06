def finder (i,arr,curr,c):
    if (len(curr) == 3):
        print (curr)
        if (len(set(curr))==3) and curr[0]!=0:
            return 1
        return 0
    if i==len(arr):
        return 0
    
    curr.append(arr[i])
    left = finder(i+1,arr,curr,c)
    curr.pop()
    right = finder(i+1,arr,curr,c)
    return left+right
arr=[1,2,3,4]
print(finder(0,arr,[],0))
