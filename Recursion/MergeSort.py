def Merge(arr,low,mid,high):

    left = low 
    right = mid+1
    arr1=[]
    while (left<=mid and right<=high):
        if(arr[left]>=arr[right]):
            arr1.append(arr[left])
            left+=1
        else:
            arr1.append(arr[right])
            right+=1
    if (left>mid):
        for i in range(right,high+1):
            arr1.append(arr[i])
    else:
        for i in range(left,mid+1):
            arr1.append(arr[i])
    y=0
    for i in range(low,high+1):
        arr[i]=arr1[y]
        y+=1
    return
        
        
def split(arr,low,high):
    if (low >= high):
        return 
    mid = (low+high)//2

    split(arr,low,mid)
    split(arr,mid+1,high)
    Merge(arr,low,mid,high)
    
arr=[2,1,4,2,4,5]
split(arr,0,len(arr)-1)
print(arr)
