def reverse(i,j,arr):
    if (i>=j):
        return 
    else:
        arr[i],arr[j]=arr[j],arr[i]
        reverse(i+1,j-1,arr)
arr=[1,2,3,4,5,6,7,8]
print(arr)
reverse(0,len(arr)-1,arr)
print(arr)